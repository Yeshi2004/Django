from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank = True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content