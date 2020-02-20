from django.db import models
from django.contrib.auth.models import User


class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    title = models.CharField(max_length=256, db_index=True)
    body = models.TextField(max_length=8000)
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['pub_date', 'user']),
        ]
