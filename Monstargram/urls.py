from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^resources/$', views.ResourceList.as_view()),
    url(r'^user_comments/$',views.UserCommentList.as_view()),
    url(r'^user_likes/$', views.UserLikesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

