from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from embed_video.fields import EmbedVideoField


UserModel = get_user_model()


class Video(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.RESTRICT, default='1')
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=600)
    upload_date = models.DateTimeField(default=timezone.now)
    url = EmbedVideoField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video-detail", kwargs={"pk": self.pk})