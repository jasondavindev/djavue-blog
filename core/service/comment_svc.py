from core.models import Comment
from commons.django_views_utils import ajax_login_required

def create_comment(comment, author, post_id):
  comment = Comment(comment=comment, post_id=post_id, author=author)
  comment.save()
  return comment.toJSON()

def get_comments(post_id):
  comments = Comment.objects.filter(post_id=post_id)
  dictComments = [comment.toJSON() for comment in comments]
  return { 'comments': dictComments }