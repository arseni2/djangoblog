from django.contrib.auth.models import AbstractUser 
from django.db import models
from django.urls import reverse

class CustomUser(AbstractUser):
    age=models.PositiveIntegerField(null=True, blank=True)

class Arcticle(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    body = models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')

