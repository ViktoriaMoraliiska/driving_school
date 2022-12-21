from django.urls import path, include

from driving_school.videos.views import GeneralVideoListView, VideoDetailView, VideoUpdateView, VideoDeleteView, \
    VideoCreateView

urlpatterns = (
    path('', GeneralVideoListView.as_view(), name='videos'),
    path('<int:pk>/', include([
        path('update/', VideoUpdateView.as_view(), name="video-update"),
        path('delete/', VideoDeleteView.as_view(), name="video-delete"),
        path('add/', VideoCreateView.as_view(), name="video-create"),
        ]))
    )


