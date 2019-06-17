# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, todo_svc, post_svc, comment_svc
from django.views.decorators.csrf import csrf_exempt


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated():
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def create_account(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    result = auth.models.User.objects.create_user(
        username, email=email, password=password, first_name=first_name, last_name=last_name)

    return JsonResponse(_user2dict(result), safe=False)


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated() else {'authenticated': False}
    return JsonResponse(i_am)


def posts(request, id=None):
    if request.method.lower() == 'post':
        return JsonResponse(post_svc.create_post(
            request.POST['title'], request.POST['body'], request.user), safe=False)

    elif request.method.lower() == 'get' and id != None:
        return JsonResponse(post_svc.get_post(id))

    elif request.method.lower() == 'delete' and id:
        return JsonResponse(post_svc.delete_post(id), safe=False)
    return JsonResponse({'posts': post_svc.get_all_posts()}, safe=False)


def comments(request, id=None):
    if request.method.lower() == 'post':
        comment = request.POST['comment']
        post_id = request.POST['post']
        return JsonResponse(comment_svc.create_comment(comment, request.user, post_id), safe=False)
    elif id != None:
        return JsonResponse({'comments': comment_svc.get_comments(id)}, safe=False)
    return JsonResponse({})

def my_posts(request):
    return JsonResponse({ 'posts': post_svc.get_my_posts(request.user) }, safe=False)

@ajax_login_required
def add_todo(request):
    todo = todo_svc.add_todo(request.POST['new_task'])
    return JsonResponse(todo)


@ajax_login_required
def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({'todos': todos})


def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d
