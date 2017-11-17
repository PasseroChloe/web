from rest_framework import serializers
from .models import User, Resource, UserComment, UserLikes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'phone_number')


class UserQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'phone_number')


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ('author', 'resource_title', 'resource_image', 'upload_time')


class UserCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserComment
        fields = ('author', 'resource', 'content', 'comment_time')


class UserLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLikes
        fields = ('user', 'resource', 'update_time')
