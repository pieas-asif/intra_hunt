from django.urls import path

from .views import home_page, landing_page

urlpatterns = [
    path('landing/', landing_page, name='landing'),
    path('', home_page, name='home'),
]