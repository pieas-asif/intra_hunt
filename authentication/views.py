from django.shortcuts import render


def auth_home_view(request):
    return render(request, 'authentication/home.html')
