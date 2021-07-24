from django.urls import path

from .views import auth_home_view

urlpatterns = [
    path('', auth_home_view, name="auth_home")
]