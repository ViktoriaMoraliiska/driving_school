from django.urls import path

from driving_school.common.views import index, about_us_view

urlpatterns = (
    path('', index, name='index'),
    path('about/', about_us_view, name='about_us'),
)
