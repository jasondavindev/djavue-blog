from commons.django_views_utils import ajax_login_required
from django.http.response import JsonResponse
from core.service import comment_svc

def switch_comment_action(request, id=None):
  if request.method.lower() == 'post':
    return create_comment(request, request.POST['comment'], request.user, request.POST['post'])

  elif id:
    return get_comments(id)
      
  return {}

def get_comments(post_id):
  return comment_svc.get_comments(post_id)

@ajax_login_required
def create_comment(request, comment, author, post_id):
  return comment_svc.create_comment(comment, author, post_id)