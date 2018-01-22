from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Topic(models.Model):
    '''学习的主题'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Entry(models.Model):
    '''具体内容'''
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + '...'
