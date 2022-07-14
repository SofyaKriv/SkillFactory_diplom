from django.forms import ModelForm
from app.models import UserProfile
from videoApp.models import Video
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from allauth.account.forms import SignupForm
from django.utils.translation import gettext, gettext_lazy as _


class PostsForm(ModelForm):
    text_post = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Video
        fields = ('author', 'title', 'video')


class SearchForm(ModelForm):
    class Meta:
        model = Video
        fields = ('author', 'video')


class BasicSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(BasicSignupForm, self).__init__(*args, **kwargs)
        self.fields['phone'] = forms.CharField(required=True)

    def save(self, request):
        phone = self.cleaned_data.pop('phone')
        user = super(BasicSignupForm, self).save(request)
        UserProfile.objects.create(user=user)
        return user
