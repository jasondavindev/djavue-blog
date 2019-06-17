from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/dapau$', views.dapau),

    # user
    url(r'^api/login$', views.login),
    url(r'^api/logout$', views.logout),
    url(r'^api/whoami$', views.whoami),
    url(r'^api/signup$', views.create_account),

    # post
    url(r'api/posts$', views.posts),
    url(r'api/posts/(?P<id>\d+)$', views.posts),
    url(r'api/posts/(?P<id>\d+)/like$', views.like_post),
    url(r'api/my-posts$', views.my_posts),

    # comment
    url(r'api/comments$', views.comments),
    url(r'api/posts/(?P<id>\d+)/comments$', views.comments),
]
