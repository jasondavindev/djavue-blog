from core.models import Post
from django.contrib.auth.models import User
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required

def switch_post_action(request, id=None):
  if request.method.lower() == 'post':
    return create_post(request, request.POST['title'], request.POST['body'], request.user)

  elif request.method.lower() == 'get' and id:
    return get_post(id)

  elif request.method.lower() == 'delete' and id:
    return delete_post(request, id)

  return { 'posts': get_all_posts() }

@ajax_login_required
def create_post(request, title, body, user):
  post = Post(title=title, body=body, author=user)
  post.save()

  return post.toJSON()

def get_all_posts():
  posts = Post.objects.all()
  return [post.toJSON() for post in posts]

def get_post(id):
  post = get_or_none(Post, pk=id)

  if post:
    return { 'post': post.toJSON() }

  return {}

@ajax_login_required
def delete_post(request, id):
  post = get_or_none(Post, pk=id)

  if post:
    post.delete()
    return { 'deleted': True, 'post': id }

  return { 'deleted': False }

def get_my_posts(author):
  posts = Post.objects.filter(author=author)
  postsDict = [post.toJSON() for post in posts]
  return { 'posts': postsDict }

def like_post(id):
  post = get_or_none(Post, pk=id)

  if post:
    post.likes += 1
    post.save()
    return { 'liked': True }
  
  return { 'liked': False }
  