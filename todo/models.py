from django.db import models


# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=200)
    priority = models.CharField(max_length=20)
    isCompleted = models.BooleanField(default=False)
