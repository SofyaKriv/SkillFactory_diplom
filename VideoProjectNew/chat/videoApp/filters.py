from django_filters import FilterSet
from .models import *
import django_filters
from django import forms


class VideoFilter(FilterSet):
    author = django_filters.CharFilter(
        field_name='author__username',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
    )
    video = django_filters.CharFilter(
        field_name='video__title_post',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
    )

    class Meta:
        model = Video
        fields = ['video', 'author']
