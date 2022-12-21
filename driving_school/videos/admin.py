from django.contrib import admin
from django.contrib.admin import ModelAdmin

from driving_school.videos.models import Video


@admin.register(Video)
class VideoAdmin(ModelAdmin):
    pass
