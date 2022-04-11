from django.db import models
from django.contrib.auth.models import User
import json
from PIL import Image

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
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.ImageField(null=True, blank=True, upload_to='images/profile/')
  bio = models.TextField(max_length=240)

  def __str__(self):
    return self.user.username

  # resizing images
  # def save(self, *args, **kwargs):
  #       super().save()

  #       img = Image.open(self.avatar.path)

  #       if img.height > 100 or img.width > 100:
  #           new_img = (100, 100)
  #           img.thumbnail(new_img)
  #           img.save(self.avatar.path)
# class RestaurantModels(models.Model):
#   name = models.CharField(max_length=240)
#   address = models.CharField(max_length=240)
#   phone = models.CharField(max_length=15)
  
#   def __str__(self):
#     return self.name

