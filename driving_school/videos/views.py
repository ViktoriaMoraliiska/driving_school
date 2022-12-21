from django.contrib.auth import get_user_model
from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import DetailView, DeleteView, UpdateView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from driving_school.videos.forms import VideoBaseForm
from driving_school.videos.models import Video

UserModel = get_user_model()


class VideoCreateView(LoginRequiredMixin, CreateView):
    model = Video
    success_url = reverse_lazy('index')
    template_name = 'videos/video-add-page.html'
    #fields = ('title', 'description','video')
    form_class = VideoBaseForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GeneralVideoListView(ListView):
    model = Video
    template_name = 'videos/video-list.html'
    context_object_name = 'videos'
    ordering = ['-upload_date']


class VideoUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Video
    template_name = 'videos/video-edit-page.html'
    success_url = "/"
    fields = ['title','description','video']

    def form_valid(self, form):
        form.instance.streamer = self.request.user
        return super().form_valid(form)

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.streamer:
            return True
        return False


class VideoDetailView(DetailView):
    template_name = "videos/video-details-page.html"
    model = Video


class VideoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "videos/video-delete-page.html"
    success_url = "/"
    model = Video

    def test_func(self):
        video = self.get_object()
        if self.request.user == video.streamer:
            return True
        return False
