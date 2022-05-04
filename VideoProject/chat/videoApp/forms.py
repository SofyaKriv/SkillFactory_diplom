from django.forms import ModelForm
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostsForm(ModelForm):
    text_post = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Video
        fields = ('author', 'title', 'category', 'video')


class SearchForm(ModelForm):
    class Meta:
        model = Video
        fields = ('author', 'video')

