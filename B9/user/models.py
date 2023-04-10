from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    def __str__(self):
        return f'{self.username} : {self.first_name}{self.last_name}'

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    