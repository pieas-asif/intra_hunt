from django.db import models


class Newsletter(models.Model):
    email_field = models.EmailField()