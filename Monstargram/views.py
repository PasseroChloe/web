from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import User, Resource, UserComment, UserLikes
from .serializers import UserSerializer, UserQuerySerializer, ResourceSerializer, UserCommentSerializer, UserLikesSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def user_list(request, format=None):
    """
    list all the users, or create a user
    :param request:
    :return:
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
    """
    read, update or delete a user instance
    :param request:
    :param pk:
    :return:
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserQuerySerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserQuerySerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def resource_list(request):
    """
    list all the resources, or create a resource
    :param request:
    :return:
    """
    if request.method == 'GET':
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def user_comment_list(request):
    """
    list all the user comments, or create a user comment
    :param request:
    :return:
    """
    if request.method == 'GET':
        user_comments = UserComment.objects.all()
        serializer = UserCommentSerializer(user_comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def user_likes_list(request):
    if request.method == 'GET':
        user_likes = UserLikes.objects.all()
        serializer = UserLikesSerializer(user_likes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserLikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
