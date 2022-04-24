from .models import *
from rest_framework import serializers


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
       model = Video
       fields = ['id', 'name', 'text']