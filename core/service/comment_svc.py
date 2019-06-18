from core.models import Comment
from commons.django_views_utils import ajax_login_required


def switch_comment_action(request, id=None):
  if request.method.lower() == 'post':
    return create_comment(request, request.POST['comment'], request.user, request.POST['post'])

  elif id:
    return { 'comments': get_comments(id) }
      
  return {}

@ajax_login_required
def create_comment(request, comment, author, post_id):
  comment = Comment(comment=comment, post_id=post_id, author=author)
  comment.save()
  return comment.toJSON()

def get_comments(post_id):
  comments = Comment.objects.filter(post_id=post_id)
  return [comment.toJSON() for comment in comments]