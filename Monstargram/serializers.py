from django.contrib.auth.models import User

from rest_framework import serializers

from .models import User, Resource, UserComment, UserLikes


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('exclude', None)
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            excludes = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing:
                if field_name in excludes:
                    self.fields.pop(field_name)


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone_number')


class ResourceSerializer(DynamicFieldsModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Resource
        fields = (
            'id',
            'author',
            'resource_title',
            'resource_image',
            'upload_time'
        )


class UserQuerySerializer(DynamicFieldsModelSerializer):
    resources = ResourceSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'phone_number',
            'resources')


class UserResourceSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Resource
        fields = (
            'id',
            'resource_title',
            'resource_image',
            'upload_time'
        )


class UserCommentSerializer(DynamicFieldsModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    resource = serializers.ReadOnlyField(source='resource.resource_title')

    class Meta:
        model = UserComment
        fields = ('id', 'author', 'resource', 'content', 'comment_time')


class UserLikesSerializer(DynamicFieldsModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    resource = serializers.ReadOnlyField(source='resource.resource_title')

    class Meta:
        model = UserLikes
        fields = ('id', 'user', 'resource', 'update_time')
