from django.http import Http404, JsonResponse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

from .models import User, Resource, UserComment, UserLikes
from .serializers import UserSerializer, UserQuerySerializer, UserResourceSerializer, ResourceSerializer, UserCommentSerializer, UserLikesSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.


class UserList(APIView):
    """
    list all the users, or create a user
    """

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    read, update or delete a user instance
    """

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserQuerySerializer(user)
        res = serializer.data
        return Response(res)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserQuerySerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ResourceList(APIView):
    """
    list all the resources, or create a resource
    """

    parser_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request, format=None):
        resources = Resource.objects.all().order_by("-upload_time")
        username_list = []
        for i in resources:
            username_list.append(i.author.username)
        serializer = ResourceSerializer(resources, many=True)
        resource_detail = []
        num = 0
        for x in serializer.data:
            x['username'] = username_list[num]
            x['likes_num'] = UserLikes.objects.filter(
                resource_id=x['id']).count()
            comment_detail = UserComment.objects.filter(resource_id=x['id'])
            comment_serializer = UserCommentSerializer(
                comment_detail, many=True)
            x['comment'] = comment_serializer.data
            resource_detail.append(x)
            num += 1
        return Response(resource_detail)

    def post(self, request, format=None):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserCommentList(APIView):
    """
    list all the user comments, or create a user comment
    """

    def get(self, request, format=None):
        user_comments = UserComment.objects.all().order_by("-comment_time")
        serializer = UserCommentSerializer(user_comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLikesList(APIView):
    """
    list all the user likes, or create a user comment
    """

    def get(self, request, format=None):
        user_likes = UserLikes.objects.all()
        serializer = UserLikesSerializer(user_likes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserLikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    def post(self, request, format=None):
        try:
            check_username = User.objects.get(
                username=request.data['username'])
        except Exception as e:
            user_not_exist_res = {
                'status': 0, 'message': "No such user exists!"}
            return JsonResponse(user_not_exist_res, safe=False)

        user_password = request.data['password']
        if(check_username.password == user_password):
            password_match_res = {
                'status': 1,
                'message': 'Login successfully!',
                'data': {
                    'user_id': check_username.pk,
                    'username': check_username.username,
                    'user_phone_number': check_username.phone_number,
                    'user_email': check_username.email}}
            return JsonResponse(password_match_res, safe=False)
        else:
            password_wrong_res = {'status': 0, 'message': 'Password is wrong!'}
            return JsonResponse(password_wrong_res, safe=False)


class Likes(APIView):
    def post(self, request, format=None):
        check_user_likes = UserLikes.objects.get(
            user=request.data['user'],
            resource=request.data['resource'])
        if check_user_likes:
            user_likes_succeed = {
                'status': 1,
                'message': 'Likes operation completed successfully!'}
            return JsonResponse(user_likes_succeed, safe=False)
        else:
            user_likes_failed = {'status': 0,
                                 'message': 'Likes operation has failed!'}
            return JsonResponse(user_likes_failed, safe=False)


class CancelLikes(APIView):
    def delete(self, request, format=None):
        cancel_user_likes = UserLikes.objects.filter(
            user=request.data['user'],
            resource=request.data['resource'])
        if cancel_user_likes:
            cancel_user_likes_succeed = {
                'status': 1,
                'message': 'Cancel likes operation completed successfully!'}
            return JsonResponse(cancel_user_likes_succeed, safe=False)
        else:
            cancel_user_likes_failed = {
                'status': 0, 'message': 'Cancel likes operation has failed!'}
            return JsonResponse(cancel_user_likes_failed, safe=False)
