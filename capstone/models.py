from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    body = models.TextField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    task_date = models.DateTimeField()
    completion_date = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.username,
            "body": self.body,
            "task_date": self.task_date.strftime("%b %d %Y, %I:%M %p"),
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
        }