from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    content = models.TextField()
    news_image = models.ImageField(upload_to='news/images/', default='media/images/logo.png') 
    news_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_details',kwargs ={'pk': self.pk})


class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    notice_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice_details',kwargs ={'pk': self.pk})