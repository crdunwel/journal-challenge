from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    body = models.CharField(max_length=8000)
    pub_date = models.DateTimeField('date published', auto_now_add=True)


