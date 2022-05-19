from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import json
from PIL import Image

from .ret_func import get_rest_name

# Create your models here.
class CommentModel(models.Model):
  comment = models.CharField(max_length=240)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.comment

class ReplyModel(models.Model):
  reply = models.CharField(max_length=240)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.ForeignKey(CommentModel, on_delete=models.CASCADE)

  def __str__(self):
    return self.reply
  
class Profile(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  avatar = models.ImageField(null=True, blank=True, upload_to='images/profile/')
  bio = models.TextField(max_length=240)

  def __str__(self):
    return str(self.user)

  def get_absolute_url(self):
    return reverse('plans')

RESTAURANT_CHOICES = [tuple([x,x]) for x in get_rest_name()]
INTEGER_CHOICES = [tuple([x,x]) for x in range(1,30)]

class Plan(models.Model):
  name = models.CharField(max_length=240, choices=RESTAURANT_CHOICES)
  title = models.CharField(max_length=240)
  date = models.DateField()
  time = models.TimeField()
  guests = models.IntegerField(choices=INTEGER_CHOICES)
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title


