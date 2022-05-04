# from django.conf.urls import url
# from app import views as app_views
# from chat import views as chat_views
# import allauth.account.views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # url('videos/$', app_views.VideoList.as_view(), name='videos'),
    # url(r'^videos/(?P<pk>\d+)$', app_views.VideoDetail.as_view(), name='video-detail'),
    # url('categories/$', app_views.CategoryList.as_view(), name='categories'),
    # url(r'^categories/(?P<pk>\d+)$', app_views.CategoryDetail.as_view(), name='category-detail'),
    # url('create/$', app_views.PostsCreateView.as_view(), name='video_create'),
    #
    # url('accounts/login/', allauth.account.views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # url('accounts/logout/', allauth.account.views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    # url('talk', chat_views.chat_view, name='chats'),
    # url('talk/<int:sender>/<int:receiver>', chat_views.message_view, name='chat'),
    # url('api/messages/<int:sender>/<int:receiver>', chat_views.message_list, name='message-detail'),
    # url('api/messages', chat_views.message_list, name='message-list'),
    # url('api/users/<int:pk>', chat_views.user_list, name='user-detail'),
    # url('api/users', chat_views.user_list, name='user-list'),
    # # url('logout', LogoutView.as_view(next_page='index'), name='logout'),
    # url('<int:pk>', chat_views.about_view, name='about'),
    # url('register', chat_views.register_view, name='register'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
