from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from driving_school.booking.forms import BookingForm


class BookingView(FormView):
    template_name = 'booking/booking-form.html'
    form_class = BookingForm
    success_url = reverse_lazy('booking success')

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)


def booking_success_view(request):
    return render(request, 'booking/booking-success-page.html')
