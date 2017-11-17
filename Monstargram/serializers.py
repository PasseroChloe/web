from rest_framework import serializers
from .models import User, Resource, UserComment, UserLikes


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=100)
    username = serializers.CharField(max_length=60)
    password = serializers.CharField(max_length=64)
    phone_number = serializers.CharField(max_length=20, allow_null=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.save()
        return instance


class ResourceSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    author = serializers.CharField(max_length=60)
    resource_title = serializers.CharField(max_length=160)
    resource_image = serializers.ImageField(allow_null=True)
    upload_time = serializers.DateTimeField('date the resource uploaded')

    def create(self, validated_data):
        return Resource.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.resource_title = validated_data.get('resource_title', instance.resource_title)
        instance.resource_image = validated_data.get('resource_image', instance.resource_image)
        instance.upload_time = validated_data.get('upload_time', instance.upload_time)


class UserCommentSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    author = serializers.CharField(max_length=60)
    resource = serializers.CharField(max_length=160)
    content = serializers.CharField(max_length=600)
    comment_time = serializers.DateTimeField('date when the user made this comment')

    def create(self, validated_data):
        return UserComment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.resource = validated_data.get('resource', instance.resource)
        instance.content = validated_data.get('content', instance.content)
        instance.comment_time = validated_data.get('comment_time', instance.comment_time)


class UserLikesSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    user = serializers.CharField(max_length=60)
    resource = serializers.CharField(max_length=160)
    update_time = serializers.DateTimeField('date when the user click at this')

    def create(self, validated_data):
        return UserLikes.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.author)
        instance.resource = validated_data.get('resource', instance.resource)
        instance.update_time = validated_data.get('update_time', instance.update_time)







