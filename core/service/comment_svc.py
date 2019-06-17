from core.models import Comment

def create_comment(comment, author, post_id):
  comment = Comment(comment=comment, post_id=post_id, author=author)
  comment.save()
  return comment.toJSON()

def get_comments(post_id):
  comments = Comment.objects.filter(post_id=post_id)
  return [comment.toJSON() for comment in comments]