from django.contrib.auth.views import LogoutView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from videoApp import views as app_views
from app import views as chat_views


urlpatterns = [
    path('', chat_views.index, name='index'),
    path('chat', chat_views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>', chat_views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>', chat_views.message_list, name='message-detail'),
    path('api/messages', chat_views.message_list, name='message-list'),
    path('api/users/<int:pk>', chat_views.user_list, name='user-detail'),
    path('api/users', chat_views.user_list, name='user-list'),
    path('logout', LogoutView.as_view(next_page='index'), name='logout'),
    path('<int:pk>', chat_views.about_view, name='about'),
    path('register', chat_views.register_view, name='register'),
    path('chat/create', chat_views.roomcreate_view, name='room_create'),
    path('api/rooms/', chat_views.room_list, name='roomlist'),
    path('chat/rooms/', chat_views.rooms_view, name='room-list'),
    path('chat/rooms/<int:pk>', chat_views.room, name='room_detail'),

    path('chat/rooms/subscribe/<int:pk>', chat_views.subscribe_me),
    path('chat/rooms/unsubscribe/<int:pk>', chat_views.unsubscribe_me),

    path('videos/$', app_views.VideoList.as_view(), name='videos'),
    path(r'^videos/(?P<pk>\d+)$', app_views.VideoDetail.as_view(), name='video-detail'),
    path('categories/$', app_views.CategoryList.as_view(), name='categories'),
    path(r'^categories/(?P<pk>\d+)$', app_views.CategoryDetail.as_view(), name='category-detail'),
    path('create/$', app_views.PostsCreateView.as_view(), name='video_create'),
    path('author/<int:pk>', app_views.author_view, name='author'),
]
