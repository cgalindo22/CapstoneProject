from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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
    fields = ("first_name", "last_name", "username", "email",
              "password1", "password2")

  def save(self, commit=True):
    user = super(RegForm, self).save(commit=False)
    user.email = self.cleaned_data["email"]
    if commit:
      user.save()
    return user

class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(UserChangeForm):
    # avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = models.Profile
        fields = ['email', 'first_name', 'last_name']

