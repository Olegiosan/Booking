from django.urls import path, include
from . import views

urlpatterns = [
    path('rooms', views.room_list, name='room_list'),
    path('rooms/<int:id>', views.room_detail, name='room_detail'),
    path('rooms/create', views.create_room, name='create_room'),
    path('', views.intro, name="intro")
]