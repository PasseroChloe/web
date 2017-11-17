from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_list', views.get_user_list),
    url(r'^resource_list', views.get_resource_list),
    url(r'^user_comment_list', views.get_user_comment_list),
    url(r'^user_likes_list', views.get_user_likes_list),
]
