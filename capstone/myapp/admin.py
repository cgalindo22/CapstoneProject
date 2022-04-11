from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CommentModel)
admin.site.register(models.ReplyModel)
admin.site.register(models.Profile)
# admin.site.register(models.RestaurantModels)
