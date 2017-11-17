from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9]+)$', views.user_detail),
    url(r'^resources/$', views.resource_list),
    url(r'^user_comments/$',views.user_comment_list),
    url(r'^user_likes/$', views.user_likes_list),
]

urlpatterns = format_suffix_patterns(urlpatterns)

