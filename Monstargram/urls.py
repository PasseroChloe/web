from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    url(r'^user_list/$', views.UserList.as_view()),
    url(r'^user_detail/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^resource_list/$', views.ResourceList.as_view()),
    url(r'^user_comment_list/$', views.UserCommentList.as_view()),
    url(r'^user_likes_list/$', views.UserLikesList.as_view()),
    url(r'^login/$', views.Login.as_view()),
    url(r'^likes/$', views.Likes.as_view()),
    url(r'^cancel_likes/$', views.CancelLikes.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
