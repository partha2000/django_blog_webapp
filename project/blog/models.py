from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Posts(models.Model):
    title = models.CharField(max_length= 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)

    # Author shares a many one relationship here wiht the post
    author = models.ForeignKey(User, on_delete = models.CASCADE)