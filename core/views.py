# coding: utf-8
import json
from django.http.response import JsonResponse
from django.contrib import auth
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, user_svc
from django.views.decorators.csrf import csrf_exempt
from core.controllers import post_ctrl, comment_ctrl


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
    return JsonResponse(post_ctrl.switch_post_action(request, id), safe=False)

def like_post(request, id):
    return JsonResponse(post_ctrl.like_post(request, id), safe=False)


def comments(request, id=None):
    return JsonResponse(comment_ctrl.switch_comment_action(request, id), safe=False)

def my_posts(request):
    return JsonResponse(post_ctrl.get_my_posts(request.user), safe=False)
