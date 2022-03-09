from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models

def must_be_gt_eight(value):
  if len(value) < 8:
    raise forms.ValidationError("Must be more than 8 characters.")
  return value

def must_be_unique(value):
  user = User.objects.filter(email=value)
  if len(user) > 0:
    raise forms.ValidationError("Email Already in Use.")
  return value

class CommentForm(forms.Form):
  comment = forms.CharField(
    label='Comment',
    required=True,
    max_length=240,
    # validators=[validate_slug],
  )
  def save(self, request):
    comment_instance = models.CommentModel()
    comment_instance.comment = self.cleaned_data["comment"]
    comment_instance.author = request.user
    comment_instance.save()
    return comment_instance

class RegForm(UserCreationForm):
  email = forms.EmailField(
    label="Email",
    required=True,
    validators=[must_be_unique],
  )

  class Meta:
    model = User
    fields = ("username", "email",
              "password1", "password2")

  def save(self, commit=True):
    user = super(RegForm, self).save(commit=False)
    user.email = self.cleaned_data["email"]
    if commit:
      user.save()
    return user
