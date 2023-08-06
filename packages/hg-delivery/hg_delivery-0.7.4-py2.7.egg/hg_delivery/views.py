#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2014  Stéphane Bard <stephane.bard@gmail.com>
#
# This file is part of hg_delivery
#
# hg_delivery is free software; you can redistribute it and/or modify it under the
# terms of the M.I.T License.
#

from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError, IntegrityError
from sqlalchemy.orm import joinedload
from collections import OrderedDict

from .models import (
    DBSession,
    Project,
    RemoteLog,
    User,
    Acl,
    Task,
    Group,
    )
from hg_delivery.nodes import (
    NodeException,
    HgNewBranchForbidden,
    HgNewHeadsForbidden,
    NodeController,
    )

import paramiko
import logging

logging.getLogger("paramiko").setLevel(logging.WARNING)

import time
import logging
import re 

log = logging.getLogger(__name__)

#------------------------------------------------------------------------------

@view_config(route_name='user_update', renderer='json', permission='edit')
def update_user(request):
    """
    update user ...
    """
    user_id = request.matchdict['id']

    user = DBSession.query(User)\
                    .filter(User.id==user_id)\
                    .scalar()

    result = False

    if user is not None :

      try :
        for attribute in request.params :
          setattr(user, attribute, request.params[attribute])
        DBSession.flush()
        result = True
        explanation = u'This user : %s (%s) has been updated ...'%(request.params['name'], request.params['email'])
      except IntegrityError as e:
        DBSession.rollback()
        result = False
        explanation = u"You can't update this user, this email is already used (%s %s) ..."%(request.params['name'], request.params['email'])

    else :
      explanation = u"This user is unknown or has already been deleted"

    return {'result'      : result,
            'explanation' : explanation}

#------------------------------------------------------------------------------

@view_config(route_name='user_delete', renderer='json', permission='edit')
def delete_user(request):
    """
    delete user ...
    """
    user_id = request.matchdict['id']
    user = DBSession.query(User)\
                    .filter(User.id==user_id)\
                    .scalar()

    result = False
    if user :
      DBSession.delete(user)
      result = True

    return {'result':result}

#------------------------------------------------------------------------------

@view_config(route_name='user_get', renderer='json', permission='edit')
def get_user(request):
    """
    delete user ...
    """
    user_id = request.matchdict['id']
    user = DBSession.query(User)\
                    .filter(User.id==user_id)\
                    .scalar()
    result = True

    return {'result' : result,
            'user'   : user}

#------------------------------------------------------------------------------

@view_config(route_name='user_add', renderer='json', permission='edit')
def add_user(request):
    """
    manage users ...
    """
    result = False
    explanation = None

    name = request.params['name']
    email = request.params['email']
    password = request.params['pwd']

    # email is the key, and password cannot be empty
    if not name :
      explanation = u'Your user profile should contain a valid name'
      result = False
    elif not email or not re.match('[^@]+@[^@]+',email):
      explanation = u'Your user profile should contain a valid email'
      result = False
    elif not password:
      explanation = u"Your user profile musn't be empty"
      result = False
    else:
      try :
        # folder should be unique
        user = User(**request.params)
        DBSession.add(user)
        DBSession.flush()
        result = True
        explanation = u'This user : %s (%s) has been added ...'%(name, email)
      except IntegrityError as e:
        DBSession.rollback()
        result = False
        explanation = u'This user and this email are already defined (%s %s) ...'%(name, email)

    return { 'result'      : result,
             'explanation' : explanation }

#------------------------------------------------------------------------------

@view_config(route_name='users_json', renderer='json', permission='edit')
@view_config(route_name='users', renderer='templates/users.mako', permission='edit')
def manage_users(request):
    """
    manage users ...
    retrieve and publish user list and project list
    """
    lst_users = DBSession.query(User).all()
    return {'lst_users':lst_users}

#------------------------------------------------------------------------------

@view_config(route_name='contact', renderer='templates/contact.mako')
def contact(request):
    """
    contact information
    """
    return {}

#------------------------------------------------------------------------------

@view_config(route_name='home', renderer='templates/index.mako')
def default_view(request):
    """
    """
    dashboard_list = []
    nodes_description = {}
    projects_list = []

    if request.authenticated_userid :
      projects_list = []
      if request.registry.settings['hg_delivery.default_login'] == request.authenticated_userid :
        projects_list = DBSession.query(Project).order_by(Project.name.desc()).all()
      else :
        projects_list = DBSession.query(Project)\
                                 .join(Acl)\
                                 .join(User)\
                                 .filter(User.id==request.user.id)\
                                 .order_by(Project.name.desc())\
                                 .all()

      for project in projects_list :
        ssh_node = None
        try :
          if not project.is_initial_revision_init() :
            project.init_initial_revision()

          if project.dashboard!=1 :
            continue

          dashboard_list.append(project)

          with NodeController(project) as ssh_node :
            repository_node = ssh_node.get_current_revision_description()

            current_rev = None 
            if repository_node and 'node' in repository_node :
              current_rev = repository_node['node']
            nodes_description[project.id] = repository_node

        except NodeException as e:
          nodes_description[project.id] = {}

    return { 'projects_list':projects_list,
             'nodes_description':nodes_description,
             'dashboard_list':dashboard_list,
           }

#------------------------------------------------------------------------------

@view_config(route_name='logs', renderer='json', permission='edit')
def logs(request):
    """
    fetch all logs
    """
    lst_logs = DBSession.query(RemoteLog)\
                        .order_by(RemoteLog.creation_date.desc())\
                        .limit(50)\
                        .all()
    return { 'logs': lst_logs}

#------------------------------------------------------------------------------

@view_config(route_name='project_logs', renderer='json', permission='edit')
def project_logs(request):
  """
  fetch logs linked to a project
  """
  id_project = request.matchdict['id']

  lst_logs = DBSession.query(RemoteLog)\
                      .filter(RemoteLog.id_project==id_project)\
                      .order_by(RemoteLog.creation_date.desc())\
                      .limit(50)\
                      .all()
  
  return { 'logs': lst_logs}

#------------------------------------------------------------------------------

@view_config(route_name='project_push_test', renderer='json')
def shall_we_push(request):
  """
    test if push is available regarding to push query result
  """
  id_project = request.matchdict['id']
  id_target_project = request.matchdict['target']

  project = DBSession.query(Project).get(id_project)
  target_project = DBSession.query(Project).get(id_target_project)
  result = False
  if project and target_project :
    with NodeController(project, silent=True) as ssh_node :
      result = ssh_node.pushable(project, target_project)
  return {'result':result}

#------------------------------------------------------------------------------

@view_config(route_name='project_pull_test', renderer='json')
def shall_we_pull(request):
  """
    test if pull is available regarding to push query result
  """
  id_project = request.matchdict['id']
  id_target_project = request.matchdict['source']

  project = DBSession.query(Project).get(id_project)
  target_project = DBSession.query(Project).get(id_target_project)
  result = False
  if project and target_project :
    with NodeController(project, silent=True) as ssh_node :
      result = ssh_node.pullable(project, target_project)
  return {'result':result}

#------------------------------------------------------------------------------

@view_config(route_name='project_brothers_update_check', renderer='json')
def who_share_this_id(request):
  """
    check who is sharing this id
  """
  id_project = request.matchdict['id']
  rev = request.matchdict['rev']

  project = DBSession.query(Project).get(id_project)
  projects_list = []

  if request.registry.settings['hg_delivery.default_login'] == request.authenticated_userid :
    projects_list = DBSession.query(Project)\
                             .order_by(Project.name.desc())\
                             .all()
  else :
    projects_list = DBSession.query(Project)\
                             .join(Acl).join(User)\
                             .filter(User.id==request.user.id)\
                             .order_by(Project.name.desc())\
                             .all()

  linked_projects = [p for p in projects_list if p.rev_init is not None and p.rev_init == project.rev_init and p.id != project.id]

  projects_sharing_that_rev = []
  for __p in linked_projects:
    # we check if this rev in it ...
    with NodeController(__p, silent=True) as ssh_node :
      if ssh_node.get_revision_description(rev) :
        projects_sharing_that_rev.append(__p)
  # found linked projects
  return {'projects_sharing_that_rev':projects_sharing_that_rev}

#------------------------------------------------------------------------------

@view_config(route_name='project_push_to', renderer='json', permission='edit')
def push(request):
  """
  """
  id_project = request.matchdict['id']
  id_target_project = request.matchdict['target']

  project = DBSession.query(Project).get(id_project)
  target_project = DBSession.query(Project).get(id_target_project)

  new_branch_stop = False
  new_head_stop = False
  result = False
  force_branch = False
  lst_new_branches = []
  data = {'buff':''}

  if project and target_project :

    if 'force_branch' in request.params and request.params['force_branch']=='true':
      force_branch = True 

    ssh_node = None
    ssh_node_remote = None

    try :
      with NodeController(project) as ssh_node :
        data = ssh_node.push_to(project, target_project, force_branch)
    except HgNewBranchForbidden as e:
      # we may inform user that he cannot push ...
      # maybe add a configuration parameter to fix this
      # and send --new-branch directly on the first time
      new_branch_stop = True
      result = False

      set_local_branches = set()
      with NodeController(project, silent=True) as ssh_node :
        set_local_branches = set(ssh_node.get_branches())

      try :
        with NodeController(target_project) as ssh_node_remote :
          set_remote_branches = set(ssh_node_remote.get_branches())
          lst_new_branches = list(set_local_branches - set_remote_branches)
          data = e.value
      except :
        data = {}
    except HgNewHeadsForbidden as e:
      # we may inform user that he cannot push ...
      # maybe add a configuration parameter to fix this
      # and send --new-branch directly on the first time
      new_head_stop = True
      result = False
      lst_new_branches = [] 
      data = e.value
    else :
      result = True
  
  return {'new_branch_stop'  : new_branch_stop,
          'new_head_stop'    : new_head_stop,
          'lst_new_branches' : lst_new_branches,
          'buffer'           : data.get('buff'),
          'result'           : result}
#------------------------------------------------------------------------------

@view_config(route_name='project_pull_from', renderer='json', permission='edit')
def pull(request):
  """
  """
  id_project = request.matchdict['id']
  id_source_project = request.matchdict['source']

  project = DBSession.query(Project).get(id_project)
  source_project = DBSession.query(Project).get(id_source_project)

  with NodeController(project, silent=True) as ssh_node :
    ssh_node.pull_from(project, source_project)
  return {}

#------------------------------------------------------------------------------

@view_config(route_name='project_add', renderer='json', permission='edit')
def add_project(request):
    """
    create a new project
    """
    result = False
    explanation = None

    host = request.params['host']
    path = request.params['path']
    user = request.params['user']

    if not host :
      explanation = u'Your project should contain a valid hostname'
    elif not path :
      explanation = u'Your project should contain a valid path'
    else:
      try :
        # folder should be unique
        project = Project(**request.params)
        DBSession.add(project)
        DBSession.flush()
        project.init_initial_revision()
        result = True
        explanation = u'This project : %s@%s/%s has been added ...'%(user, host, path)
      except IntegrityError as e:
        DBSession.rollback()
        result = False
        explanation = u'This project and this path are already defined (%s %s) ...'%(host, path)

    return { 'result'      : result,
             'explanation' : explanation }

#------------------------------------------------------------------------------

@view_config(route_name='project_update', renderer='json', permission='edit')
def update_project(request):
    """
    update the project properties (host, path, password ...)
    """
    result = False
    id_project = request.matchdict['id']

    host = request.params['host']
    path = request.params['path']
    user = request.params['user']
    project = None
    explanation = None

    if not host :
      explanation = u'Your project should contain a valid hostname'
    elif not path :
      explanation = u'Your project should contain a valid path'
    else:
      try :
        project = DBSession.query(Project).get(id_project)
        for key in request.params :
          setattr(project, key, request.params[key])

        if 'dashboard' not in request.params :
          project.dashboard = 0

        DBSession.flush()
        explanation = u'This project : %s@%s/%s has been updated ...'%(user, host, path)
        result = True
      except :
        DBSession.rollback()
        result = False

    return { 'result'      : result,
             'project'     : project,
             'explanation' : explanation  }

#------------------------------------------------------------------------------

@view_config(route_name='view_file_content', permission='edit')
def get_file_content(request):
    """
    view file content regarding to revision id
    """
    id_project = request.matchdict['id']
    revision = request.matchdict['rev']
    file_name = "/".join(request.matchdict['file_name'])
    project = DBSession.query(Project).get(id_project)
    data = ""
    with NodeController(project, silent=True) as ssh_node :
      data = ssh_node.get_content(revision, file_name)
    response = Response(data)
    return response

#------------------------------------------------------------------------------

@view_config(route_name='project_delete', renderer='json', permission='edit')
def delete_project(request):
    """
    delete a project
    """
    result = False
    try :
      id_project = request.matchdict['id']
      project = DBSession.query(Project).get(id_project)
      project.delete_nodes()

      DBSession.delete(project)
      DBSession.flush()
      result = True
    except :
      DBSession.rollback()
      result = False

    return { 'result':result }

#------------------------------------------------------------------------------

@view_config(route_name='project_refresh_state', renderer='edit#publish_project_html.mako', permission='edit')
@view_config(route_name='project_edit', renderer='edit.mako', permission='read')
def edit_project(request):
    """
    """
    result = False
    id_project = request.matchdict['id']

    projects_list = []
    if request.registry.settings['hg_delivery.default_login'] == request.authenticated_userid :
      projects_list = DBSession.query(Project).order_by(Project.name.desc()).all()
    else :
      projects_list = DBSession.query(Project).join(Acl).join(User).filter(User.id==request.user.id).order_by(Project.name.desc()).all()

    projects_map = {p.id:p for p in projects_list}
    project = projects_map.get(id_project)

    delivered_hash = {}
    for l in DBSession.query(RemoteLog.command, RemoteLog.creation_date)\
                      .order_by(RemoteLog.creation_date.desc())\
                      .filter(RemoteLog.id_project==id_project)\
                      .filter(RemoteLog.command.like('%hg update -C -r%'))\
                      .limit(200) :
      if l.command.count('hg update -C -r') :
        hash_rev = l.command.split('hg update -C -r ')[1].strip()
        if hash_rev in delivered_hash :
          delivered_hash[hash_rev].append(l.creation_date)
        else :
          delivered_hash[hash_rev] = [l.creation_date]

    if project is None :
      return HTTPFound(location=request.route_url(route_name='home'))
    linked_projects = [p for p in projects_list if p.rev_init is not None and p.rev_init == project.rev_init and p.id != project.id]

    branch = None
    if 'branch' in request.params :
      branch = request.params['branch']

    tag = None
    if 'tag' in request.params :
      tag = request.params['tag']

    limit = 200 
    settings = request.registry.settings
    if 'hg_delivery.default_log_limit' in settings and settings['hg_delivery.default_log_limit'].isdigit():
      limit = int(settings['hg_delivery.default_log_limit'])

    request.registry.settings 
    if 'limit' in request.params and request.params['limit'].isdigit():
      limit = int(request.params['limit'])

    repository_error = None

    users = DBSession.query(User)
    project_acls = {_acl.id_user:_acl.acl for _acl in DBSession.query(Acl).filter(Acl.id_project == id_project)}
    project_tasks = DBSession.query(Task).filter(Task.id_project == id_project).all()

    try :
      with NodeController(project) as ssh_node :

        if not project.dvcs_release :
          project.dvcs_release = ssh_node.get_release()

        current_rev = ssh_node.get_current_rev_hash()

        last_hundred_change_list, map_change_sets = ssh_node.get_last_logs(limit, branch_filter=branch, revision_filter=tag)
        list_branches = ssh_node.get_branches()
        list_tags = ssh_node.get_tags()

        current_node = map_change_sets.get(current_rev)
        if current_node is None :
          current_node = ssh_node.get_revision_description(current_rev)
    except NodeException as e:
      repository_error = e.value
      log.error(e.value)
      current_node = None
      list_branches = []
      list_tags = []
      last_hundred_change_list, map_change_sets = [], {}

    id_user = request.authenticated_userid
    allow_to_modify_acls = False
    if request.registry.settings['hg_delivery.default_login'] == request.authenticated_userid :
      allow_to_modify_acls = True

    return { 'project'                  : project,
             'list_branches'            : list_branches,
             'list_tags'                : list_tags,
             'limit'                    : limit,
             'projects_list'            : projects_list,
             'filter_tag'               : tag,
             'filter_branch'            : branch,
             'repository_error'         : repository_error,
             'current_node'             : current_node,
             'linked_projects'          : linked_projects,
             'last_hundred_change_list' : last_hundred_change_list,
             'users'                    : users,
             'allow_to_modify_acls'     : allow_to_modify_acls,
             'project_acls'             : project_acls,
             'project_tasks'            : project_tasks,
             'knonwn_acl'               : Acl.known_acls,
             'delivered_hash'           : delivered_hash}

#------------------------------------------------------------------------------

@view_config(route_name='project_run_task', renderer='json', permission='edit')
def run_task(request):
  """
  """
  id_task = request.matchdict['id']
  task = DBSession.query(Task).get(id_task)
  result = False
  if task :
    try :
      with NodeController(task.project) as ssh_node :
        ssh_node.run_command(task.content, log=True)
    except IntegrityError as e:
      result = False
      explanation = u"wtf ?"
    else :
      result = True 

  return {'result':result}

#------------------------------------------------------------------------------

@view_config(route_name='tasks', renderer='templates/tasks.mako', permission='edit')
def view_all_tasks(request):
  """
  """
  if request.registry.settings['hg_delivery.default_login'] == request.authenticated_userid :
    tasks = DBSession.query(Task).join(Project).options(joinedload(Task.project)).order_by(Project.name.desc()).all()
  else :
    tasks = DBSession.query(Task).join(Project).join(Acl).join(User).filter(User.id==request.user.id).options(joinedload(Task.project)).order_by(Project.name.desc()).all()

  dict_project_to_tasks = OrderedDict()

  for task in tasks :
    project = task.project
    if project in dict_project_to_tasks :
      dict_project_to_tasks[project].append(task)
    else :
      dict_project_to_tasks[project] = [task]

  return {'dict_project_to_tasks':dict_project_to_tasks}

#------------------------------------------------------------------------------

@view_config(route_name='project_delete_task', renderer='json', permission='edit')
def remove_project_task(request):
  """
    remove some task on project
  """
  id_task = request.matchdict['id']
  result = False
  try :
    task = DBSession.query(Task).get(id_task)
    DBSession.delete(task)
  except IntegrityError as e:
    result = False
    explanation = u"wtf ?"
  else :
    result = True 

  return {'result':result}

#------------------------------------------------------------------------------

@view_config(route_name='project_save_tasks', renderer='json', permission='edit')
def save_project_tasks(request):
  """
  """
  id_project = request.matchdict['id']
  project = DBSession.query(Project).get(id_project)
  result = False

  if project :
    try :
      # we remove old tasks 
      project.tasks[0:] = []
      for  _task_content in request.params.getall('task_content') :
        if _task_content :
          task = Task(id_project, _task_content.strip())
          # make the link with DBSession ...
          DBSession.add(task)
          project.tasks.append(task)
      DBSession.flush()
      result = True
    except IntegrityError as e:
      DBSession.rollback()
      result = False
      explanation = u"wtf ?"

  return {'result':result, 'tasks':project.tasks}

#------------------------------------------------------------------------------

@view_config(route_name='project_save_acls', renderer='json', permission='edit')
def save_project_acls(request):
  """
  """
  id_project = request.matchdict['id']
  project = DBSession.query(Project).get(id_project)

  result = False

  if project :
    try :
      # we remove old ACLs
      project.acls[0:] = []
      for ele, _acl_label in request.params.iteritems() :
        if ele.count('projectacl') and _acl_label in Acl.known_acls:

          # create acl object
          id_user = int(ele.split('_')[1])
          acl = Acl(id_user, id_project, _acl_label)

          # make the link with DBSession ...
          DBSession.add(acl)
          project.acls.append(acl)

      DBSession.flush()
      result = True
    except IntegrityError as e:
      DBSession.rollback()
      result = False
      explanation = u"wtf ?"

  return {'result':result}

#------------------------------------------------------------------------------

@view_config(route_name='project_fetch', renderer='json', permission='edit')
def fetch_project(request):
    """
    retrieve information about a project and send result in json
    this view is usable to compare projects
    """
    result = False
    id_project = request.matchdict['id']
    project = DBSession.query(Project).get(id_project)

    branch = None
    if 'branch' in request.params :
      branch = request.params['branch']

    limit = 200
    if 'limit' in request.params and request.params['limit'].isdigit():
      limit = int(request.params['limit'])

    repository_error = None

    try :
      with NodeController(project) as ssh_node :
        current_rev = ssh_node.get_current_rev_hash()
        last_hundred_change_list, map_change_sets = ssh_node.get_last_logs(limit, branch_filter=branch)
    except NodeException as e:
      repository_error = e.value
      log.error(e)
      last_hundred_change_list, map_change_sets = [], {}

    return { 'repository_error'         : repository_error,
             'last_hundred_change_list' : last_hundred_change_list}

#------------------------------------------------------------------------------

@view_config(route_name='project_revision_details', renderer='templates/revision.mako', permission='edit')
@view_config(route_name='project_revision_details_json', renderer='json', permission='edit')
def fetch_revision(request):
  """
  """
  id_project = request.matchdict['id']
  revision = request.matchdict['rev']

  project = DBSession.query(Project).get(id_project)

  diff = ""
  revision_description = {}

  with NodeController(project, silent=True) as ssh_node :
    diff = ssh_node.get_revision_diff(revision)
    revision_description = ssh_node.get_revision_description(revision)

  return {'diff'     : diff,
          'project'  : project,
          'revision' : revision_description}

#------------------------------------------------------------------------------

@view_config(route_name='project_change_to', permission='edit', renderer='json')
def update_project_to(request):
  """
  """
  id_project = request.matchdict['id']

  brothers_id_project = request.matchdict['brother_id']
  revision = request.matchdict['rev']
  result = {}

  def move_it(project, revision, result) :
    """
      update a project to a specific revision (a hash)
    """
    with NodeController(project, silent=True) as ssh_node:

      ssh_node.update_to(revision)
      current_rev = ssh_node.get_current_rev_hash()
      stop_at = 0
      while current_rev!=revision and stop_at<10 :
        # sleep 100 ms
        time.sleep(0.100)
        current_rev = ssh_node.get_current_rev_hash()
        stop_at += 1
      if current_rev == revision :
        result[project.id] = True
      for task in project.tasks :
        ssh_node.run_command(task.content, log=True)

  project = DBSession.query(Project).get(id_project)
  if project :
    result[project.id] = False
    move_it(project, revision, result)

  for _id_project in brothers_id_project :
    project_brother = DBSession.query(Project).get(_id_project)
    if project_brother :
      result[project_brother.id] = False
      move_it(project_brother, revision, result)

  return {'result':result}

#------------------------------------------------------------------------------

