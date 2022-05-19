from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from datetime import datetime, date

from . import views
from . import models
from .ret_func import get_rest_name, get_usernames

def must_be_gt_eight(value):
  if len(value) < 8:
    raise forms.ValidationError("Must be more than 8 characters.")
  return value
 
def must_be_unique(value):
  user = User.objects.filter(email=value)
  if len(user) > 0:
    raise forms.ValidationError("Email Already in Use.")
  return value

def must_be_gt_today(value):
  print(str(value))
  print(str(date.today()))
  if str(value) < str(date.today()):
    raise forms.ValidationError("The date cannot be in the past!")
  return value

def must_be_caps(value):
  print(value.upper())
  if value != value.upper():
    raise forms.ValidationError("NEEDS TO BE ALL CAPS")
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

class UpdateUserForm(forms.ModelForm):
  first_name = forms.CharField(
    max_length=100, 
    widget=forms.TextInput(attrs={'class': 'form-control'}
  ))
  last_name = forms.CharField(
    max_length=100, 
    widget=forms.TextInput(attrs={'class': 'form-control'}
  ))
  username = forms.CharField(
    max_length=100,
    required=True,
    widget=forms.TextInput(attrs={'class': 'form-control'},
  ))
  email = forms.EmailField(
    required=True,
    widget=forms.TextInput(attrs={'class': 'form-control'},
  ))

  class Meta:
      model = User
      fields = ['first_name', 'last_name', 'username', 'email']

class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}
    ))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    class Meta:
        model = models.Profile
        fields = ['avatar', 'bio']

class ProfilePageForm(forms.ModelForm):
  class Meta:
    model = models.Profile
    fields = ('avatar', 'bio')
    widget = {
      'bio': forms.Textarea(attrs={'class':'form-control'}),
    }

class DateInput(forms.DateInput):
  input_type = 'date'


RESTAURANT_CHOICES = [tuple([x,x]) for x in get_rest_name()]
INTEGER_CHOICES = [tuple([x,x]) for x in range(1,30)]
USERS = [tuple([x,x]) for x in get_usernames()]

class PlanForm(forms.Form):
  name = forms.CharField(
    label="Name",
    required=True,
    max_length=240,
    widget=forms.Select(choices=RESTAURANT_CHOICES),
    )
  title = forms.CharField(
    label="Event Title", 
    required=True,
    max_length=240, 
    validators=[validate_slug],
    )
  date = forms.DateField(
    label="Date", 
    required=True, 
    widget=DateInput,
  )
  time = forms.TimeField(
    label="Time",
  )
  guests = forms.IntegerField(
    label="Guests",
    widget=forms.Select(choices=INTEGER_CHOICES),
  )

  def save(self, request):
    plan_inst = models.Plan()
    plan_inst.name = self.cleaned_data["name"]
    plan_inst.title = self.cleaned_data["title"]
    plan_inst.date = self.cleaned_data["date"]
    plan_inst.time = self.cleaned_data["time"]
    plan_inst.guests = self.cleaned_data["guests"]
    plan_inst.author = request.user
    plan_inst.save()
    return plan_inst
