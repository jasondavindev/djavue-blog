from commons.django_views_utils import ajax_login_required
from django.http.response import JsonResponse
from core.service import post_svc

def switch_post_action(request, id=None):
  if request.method.lower() == 'post':
    return create_post(request, request.POST['title'], request.POST['body'], request.user)

  elif request.method.lower() == 'delete' and id:
    return delete_post(request, id)
    
  elif request.method.lower() == 'get' and id:
    return get_post(id)

  return get_all_posts()


def get_all_posts():
  return post_svc.get_all_posts()

def get_post(id=None):
  return post_svc.get_post(id)

@ajax_login_required
def create_post(request, title, body, user):
  return post_svc.create_post(title, body, user)

@ajax_login_required
def delete_post(request, id):
  return post_svc.delete_post(id)

@ajax_login_required
def get_my_posts(author):
  return post_svc.get_my_posts(author)

@ajax_login_required
def like_post(request, id):
  return post_svc.like_post(id)