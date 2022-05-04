from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from app.models import UserProfile


# class UserProfile(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     followers = models.ManyToManyField('self', related_name='followers', blank=True)
#     following = models.ManyToManyField('self', related_name='following', blank=True)
#     profile_image = models.ImageField(blank=True)
#
#     def __str__(self):
#         return self.user.username


class Category(models.Model):
    theme = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.theme}'


class Video(models.Model):
    video = models.FileField(upload_to='uploads/')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    category = models.ManyToManyField(Category, through='VideoCategory')
    rate_video = models.IntegerField(default=0, null=True)
    create_date = models.DateTimeField(auto_now=True)

    def like(self):
        self.rate_video = self.rate_video + 1
        self.save()

    def dislike(self):
        self.rate_video -= Video.objects.get(id=1).rate_video
        self.save()


class VideoCategory(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    author = models.ManyToManyField(UserProfile)
    text = models.CharField(max_length=1024)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}: {}'.format(self.author, self.text)
