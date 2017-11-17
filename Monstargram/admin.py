from django.contrib import admin

from .models import User
from .models import Resource
from .models import UserComment
from .models import UserLikes

# Register your models here.
admin.site.register(User)
admin.site.register(Resource)
admin.site.register(UserComment)
admin.site.register(UserLikes)
