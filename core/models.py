from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class ActivityLog(models.Model):
    type = models.CharField(max_length=64)
    logged_user = models.ForeignKey(User, null=True, blank=True)
    fromuser = models.ForeignKey(User, null=True, blank=True, related_name="activitylogs_withfromuser")
    jsondata = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '%s / %s / %s' % (
            self.type,
            self.logged_user,
            self.created_at,
        )


class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_from_user')
    likes = models.IntegerField(default=0)

    def toJSON(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created': int(self.created.timestamp() * 1000),
            'likes': self.likes,
            'author': {
                'username': self.author.username,
                'first_name': self.author.first_name,
                'last_name': self.author.last_name,
            }
        }

class Comment(models.Model):
    comment = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_from_user')
    post_id = models.IntegerField(null=True)

    def toJSON(self):
        return {
            'id': self.id,
            'comment': self.comment,
            'created': int(self.created.timestamp() * 1000),
            'post': self.post_id,
            'author': {
                'username': self.author.username,
                'first_name': self.author.first_name,
                'last_name': self.author.last_name,
            }
        }

class Todo(models.Model):
    description = models.CharField(max_length=512)
    done = models.BooleanField(default=False)

    def to_dict_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'done': self.done,
        }
