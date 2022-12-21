from django.urls import path

from driving_school.prices.views import prices_view, add_prices_view

urlpatterns = (
    path('prices/', prices_view, name='prices'),
    path('add_price/', add_prices_view, name='add prices'),
)