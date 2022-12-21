from django.urls import path

from driving_school.booking.views import booking_success_view, BookingView

urlpatterns = (
    path('', BookingView.as_view(), name='booking form'),
    path('success/', booking_success_view, name='booking success')
)
