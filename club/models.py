from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    content = models.TextField()
    news_image = models.ImageField(upload_to='news/images/', default='media/logo.jpeg') 
    news_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_details',kwargs ={'pk': self.pk})
    

class Event(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    content = models.TextField()
    event_image = models.ImageField(upload_to='event/images/', default='media/logo.jpeg') 
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_details',kwargs ={'pk': self.pk})
    

class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    notice_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice_details',kwargs ={'pk': self.pk})
    


class Committee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    member_image = models.ImageField(upload_to='committee/images/', default='committee/images/logo.png') 
    

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('committee')
    
