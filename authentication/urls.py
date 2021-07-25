from django.urls import path

from .views import auth_home_view, register_user

urlpatterns = [
    path('register/', register_user, name="register"),
    path('', auth_home_view, name="auth_home")
]