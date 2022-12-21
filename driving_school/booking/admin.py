from django.contrib import admin
from django.contrib.admin import ModelAdmin

from driving_school.booking.models import BookingModel


@admin.register(BookingModel)
class BookingAdmin(ModelAdmin):
    pass
