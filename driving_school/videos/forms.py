from django import forms

from driving_school.videos.models import Video


class VideoBaseForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'url')

        labels = {
            'title': 'Title',
            'description': 'Description',
            'url': 'Video URL',
        }