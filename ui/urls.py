from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.my_view, name='my-view'),
    path('read/', views.read, name='read'),
    path("home/", views.home, name="home"),
    path("vo/", views.vo, name="vo"),
    path("detail/<int:id>", views.detail, name='detail'),
    url("mp4/", views.stream_video),
    url("get_text/", views.get_text),
    path("add", views.add, name='add'),
    path("edit/<int:id>", views.edit, name='edit'),
    path("search-result", views.test_filter, name='search-result')
]
