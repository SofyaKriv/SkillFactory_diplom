from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url('videos/$', views.VideoList.as_view(), name='videos'),
    url(r'^videos/(?P<pk>\d+)$', views.VideoDetail.as_view(), name='video-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
