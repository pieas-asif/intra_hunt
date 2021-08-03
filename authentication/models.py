from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    USER_TYPE_CHOICES = [
        ('CO', 'Company'),
        ('IN', 'Individual')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES)
    image = models.ImageField(default='default.png', upload_to='profile_pictures')

    def __str__(self):
        return f'{self.user.username} ({self.type}) Profile'
