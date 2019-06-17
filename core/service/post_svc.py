from core.models import Post
from django.contrib.auth.models import User

def create_post(title, body, user):
  post = Post(title=title, body=body, author=user)
  post.save()
  return post.toJSON()

def get_all_posts():
  posts = Post.objects.all()
  return [post.toJSON() for post in posts]

def get_post(id):
  try:
    post = Post.objects.get(pk=id)
    return { 'post': post.toJSON() }
  except:
    return {}

def delete_post(id):
  try:
    Post.objects.get(pk=id).delete()
    return { 'deleted': True, 'post': id }
  except:
    return { 'deleted': False }

def get_my_posts(author):
  posts = Post.objects.filter(author=author)
  return [post.toJSON() for post in posts]