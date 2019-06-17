# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, post_svc, comment_svc, user_svc
from django.views.decorators.csrf import csrf_exempt


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    return JsonResponse(user_svc.login(request, request.POST['username'], request.POST['password']), safe=False)


def logout(request):
    return JsonResponse(user_svc.logout(request), safe=False)


@csrf_exempt
def create_account(request):
    return JsonResponse(user_svc.create_account(request), safe=False)


def whoami(request):
    return JsonResponse(user_svc.whoami(request.user))


def posts(request, id=None):
    if request.method.lower() == 'post':
        return JsonResponse(post_svc.create_post(
            request.POST['title'], request.POST['body'], request.user), safe=False)

    elif request.method.lower() == 'get' and id != None:
        return JsonResponse(post_svc.get_post(id))

    elif request.method.lower() == 'delete' and id:
        return JsonResponse(post_svc.delete_post(id), safe=False)


    return JsonResponse({'posts': post_svc.get_all_posts()}, safe=False)


def like_post(request, id):
    return JsonResponse(post_svc.like_post(id), safe=False)


def comments(request, id=None):
    if request.method.lower() == 'post':
        return JsonResponse(comment_svc.create_comment(request.POST['comment'], request.user, request.POST['post']), safe=False)

    elif id:
        return JsonResponse({'comments': comment_svc.get_comments(id)}, safe=False)
        
    return JsonResponse({})


def my_posts(request):
    return JsonResponse({ 'posts': post_svc.get_my_posts(request.user) }, safe=False)
