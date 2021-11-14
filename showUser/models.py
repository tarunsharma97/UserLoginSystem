from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username