from . import views
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name="motion_index"),
    # url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]  