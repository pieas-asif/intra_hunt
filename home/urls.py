from django.urls import path
from .views import home_page, landing_page, post_page, find_work_view

urlpatterns = [
    path('test_post/', post_page, name='test-post'),
    path('find_work/', find_work_view, name='find-work'),
    path('landing/', landing_page, name='landing'),
    path('', home_page, name='home'),
]
