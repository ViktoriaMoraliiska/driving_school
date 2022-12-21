from django.contrib import admin
from django.contrib.admin import ModelAdmin

from driving_school.prices.models import CategoryPrice


@admin.register(CategoryPrice)
class PriceAdmin(ModelAdmin):
    pass