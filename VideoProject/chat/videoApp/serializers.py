from .models import *
from rest_framework import serializers


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Video
       fields = ['id', 'title', 'video']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Category
       fields = ['id', 'theme', ]


