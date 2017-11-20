from django.contrib.auth.models import User

from rest_framework import serializers

from .models import User, Resource, UserComment, UserLikes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'phone_number')


class UserQuerySerializer(serializers.ModelSerializer):
    resources = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Resource.objects.all())

    class Meta:
        model = User
        fields = ('email', 'username', 'phone_number', 'resources')


class ResourceSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Resource
        fields = ('id', 'author', 'resource_title', 'resource_image', 'upload_time')


class UserCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    resource = serializers.ReadOnlyField(source='resource.resource_title')

    class Meta:
        model = UserComment
        fields = ('author', 'resource', 'content', 'comment_time')


class UserLikesSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    resource = serializers.ReadOnlyField(source='resource.resource_title')

    class Meta:
        model = UserLikes
        fields = ('user', 'resource', 'update_time')
