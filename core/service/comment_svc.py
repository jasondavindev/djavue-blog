from core.models import Comment

def switch_comment_action(request, id=None):
  if request.method.lower() == 'post':
    return create_comment(request.POST['comment'], request.user, request.POST['post'])

  elif id:
    return { 'comments': get_comments(id) }
      
  return {}

def create_comment(comment, author, post_id):
  comment = Comment(comment=comment, post_id=post_id, author=author)
  comment.save()
  return comment.toJSON()

def get_comments(post_id):
  comments = Comment.objects.filter(post_id=post_id)
  return [comment.toJSON() for comment in comments]