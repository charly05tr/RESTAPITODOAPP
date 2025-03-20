from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Task(models.Model):
    task = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    states = [('P', 'Pendiente'), ('T', 'terminada')]
    state = models.TextField(choices=states)
    priority_choices = [('A', 'Alta'), ('M', 'Media'), ('B', 'Baja')]
    priority = models.TextField(choices=priority_choices)
    created_at = models.DateField(auto_now_add=True)
    ends_at = models.DateField(default=None)
    