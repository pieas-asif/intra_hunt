from django.contrib import admin

# Register your models here.
from home.models import Newsletter, Post

admin.site.register(Newsletter)
admin.site.register(Post)
