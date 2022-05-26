from .models import *
from rest_framework import serializers


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.CharField(required=False)

    class Meta:
       model = Video
       fields = ['id', 'title', 'video', 'author', ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    video = VideoSerializer(many=True)

    class Meta:
       model = Category
       fields = ['id', 'theme', 'video', ]


class VideoCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = VideoCategory
       fields = ['id', 'video', 'category', ]

