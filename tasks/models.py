from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    priority = models.IntegerField(default=1)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

  

