from django.conf.urls import url
from django.conf.urls import include

from . import views

app_name = 'gear'

urlpatterns = [
    url(r'^profile/', views.profile, name='profile'),
    url(r'^list/', views.list, name='list'),
    url(r'^list_detail/(?P<pk>\d+)/$', views.list_detail, name='list_detail'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete_item, name="delete_item"),
    url(r'^delete_list/(?P<pk>\d+)/$', views.delete_list, name="delete_list"),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^update/item/(?P<item_id>\d+)/$', views.update_item, name="update_item"),
]