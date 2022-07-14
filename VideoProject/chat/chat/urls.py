"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from ckeditor_uploader import views
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.conf.urls.static import static
from django.conf import settings
import videoApp.views as video_views
import app.views as app_views
from rest_framework import routers
from django.views.generic import TemplateView
from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'videos', video_views.VideoView, 'videos')
router.register(r'categories', video_views.CategoryView, 'categories')
router.register(r'videocategory', video_views.VideoCategoryView, 'videocategory')
router.register(r'messages', app_views.MessageView, 'messages')
router.register(r'users', app_views.UserView, 'users')

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/', include(router.urls)),
    path('swagger-ui/', schema_view),
    path('accounts/', include('allauth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^ckeditor/upload/', login_required(views.upload), name='ckeditor_upload'),
    url(r'^ckeditor/browse/', never_cache(login_required(views.browse)), name='ckeditor_browse'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
