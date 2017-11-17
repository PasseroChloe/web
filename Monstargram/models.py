from django.db import models
# from pygments.lexers import get_all_lexers
# from pygments.styles import get_all_styles




# Create your models here.


# LEXERS = [item for item in get_all_lexers() if item[1]]
# LANGUAGE_CHOICES = sorted([(item[1][0], item[0] for item in LEXERS)])
# STYLE_CHOICES = sorted((item, item) for item in get_all_lexers())


class User(models.Model):
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20, null=True)

    def serialize(self):
        return self.__dict__

    def __str__(self):
        return self.username


class Resource(models.Model):
    class Meta:
        verbose_name = '资源'
        verbose_name_plural = '资源'

    author = models.ForeignKey(User)
    resource_title = models.CharField(max_length=160)
    resource_image = models.ImageField(null=True)
    upload_time = models.DateTimeField('date the resource uploaded')

    def serialize(self):
        return self.__dict__

    def __str__(self):
        return self.resource_title


class UserComment(models.Model):
    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = '用户评论'
    author = models.ForeignKey(User)
    resource = models.ForeignKey(Resource, related_name='comments')
    content = models.CharField(max_length=600)
    comment_time = models.DateTimeField('date when the user made this comment')

    def serialize(self):
        return self.__dict__

    def __str__(self):
        return "username：" + str(self.author) + " | " + "resource——title: " + str(self.resource) + \
            " | " + "content: " + str(self.content) + " | " + "time: " + str(self.comment_time)


class UserLikes(models.Model):
    class Meta:
        verbose_name = '用户点赞'
        verbose_name_plural = '用户点赞'
    user = models.ForeignKey(User)
    resource = models.ForeignKey(Resource, related_name='likes')
    update_time = models.DateTimeField('date when the user click at this')

    def serialize(self):
        return self.__dict__

    def __str__(self):
        return "username：" + str(self.user) + " | " + "resource——title: " + \
            str(self.resource) + " | " + "time: " + str(self.update_time)
