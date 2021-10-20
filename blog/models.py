from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_autor = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(default=timezone.now)
    post_content = models.TextField()
