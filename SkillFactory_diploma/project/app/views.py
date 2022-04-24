from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import *
from .models import *


class VideoView(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


def index(request):
    if request.method == "GET":
        return render(request, 'index.html')


class VideoList(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'videos.html'

    def get(self, request):
        queryset = Video.objects.all()
        return Response({'videos': queryset})


class VideoDetail(generics.RetrieveAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'video.html'

    def retrieve(self, request, pk, *args, **kwargs):
        video = get_object_or_404(Video, pk=pk)
        serializer = VideoSerializer(video)
        return Response({'serializer': serializer, 'video': video})


