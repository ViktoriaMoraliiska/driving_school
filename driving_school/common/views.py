from django.shortcuts import render


def index(request):
    return render(request, 'common/home-page.html')


def about_us_view(request):
    return render(request, 'common/about.html')


