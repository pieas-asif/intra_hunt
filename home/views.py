from django.shortcuts import render


def home_page(request):
    return render(request, 'home/pages/home.html')


def landing_page(request):
    return render(request, 'home/pages/landing.html')
