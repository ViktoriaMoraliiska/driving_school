from django.shortcuts import render, redirect

from driving_school.prices.forms import PricesCreateForm
from driving_school.prices.models import CategoryPrice


def add_prices_view(request):
    if request.method == 'GET':
        form = PricesCreateForm
    else:
        form = PricesCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }
    return render(request, 'prices/add_price.html', context)


def prices_view(request):
    context = {
        'prices': CategoryPrice.objects.all()
    }

    return render(request, 'prices/prices.html', context)