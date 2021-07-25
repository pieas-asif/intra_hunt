from django.urls import path
from .views import home_page, landing_page, post_page

urlpatterns = [
    path('test_post/', post_page, name='test_post'),
    path('landing/', landing_page, name='landing'),
    path('', home_page, name='home'),
]
