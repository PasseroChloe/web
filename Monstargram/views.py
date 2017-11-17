from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import User
from .models import Resource
from .models import UserComment
from .models import UserLikes


import json

# Create your views here.


def index(request):
    resp = {'errorcode': 100, 'detail': 'Welcome to the index of Monstargram!'}
    return HttpResponse(json.dumps(resp), content_type="application/json")


def get_user_list(request):
    user_list = User.objects.all()
    user_list_serial = serializers.serialize("json", user_list)
    return JsonResponse(user_list_serial, safe=False)


def get_resource_list(request):
    resource_list = [i for i in Resource.objects.all()]
    resource_list_serial = serializers.serialize("json", resource_list)
    return JsonResponse(resource_list_serial, safe=False)


def get_user_comment_list(request):
    user_comment_list = UserComment.objects.all()
    user_comment_list_serial = serializers.serialize("json", user_comment_list)
    return JsonResponse(user_comment_list_serial, safe=False)


def get_user_likes_list(request):
    user_likes_list = UserLikes.objects.all()
    user_likes_list_serial = serializers.serialize(
        "json", user_likes_list)
    return JsonResponse(user_likes_list_serial, safe=False)
