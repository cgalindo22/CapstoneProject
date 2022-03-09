from distutils.log import debug
import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import requests
# from YelpAPI import get_my_key

from . import models
from . import forms

# Create your views here.
def logout_view(request):
  logout(request)
  return redirect("/login/")

def index(request):
  if request.method == "POST":
    if request.user.is_authenticated:
      comment_form = forms.CommentForm(request.POST)
      if comment_form.is_valid():
        comment_form.save(request)
        comment_form = forms.CommentForm()
      else:
        comment_form = forms.CommentForm()
  else:
    comment_form = forms.CommentForm()

  comment_objects = models.CommentModel.objects.all()
  comment_list = []
  for com in comment_objects:
    reply_objects = models.ReplyModel.objects.filter(comment=com)
    tmp_com = {}
    tmp_com["comment"] = com.comment
    tmp_com["id"] = com.id
    tmp_com["author"] = com.author.username
    tmp_com["replies"] = reply_objects
    comment_list+=[tmp_com]
  context = {
    "title": "Comments",
    "comments":comment_list,
    "form":comment_form,
  }
  return render(request, "index.html", context=context)

def get_comments(request):
  comment_objects = models.CommentModel.objects.all()
  comment_list = {}
  comment_list["comments"]=[]
  for com in comment_objects:
    reply_objects = models.ReplyModel.objects.filter(comment=com)
    tmp_com = {}
    tmp_com["comment"] = com.comment
    tmp_com["author"] = com.author.username
    tmp_com["id"] = com.id
    tmp_com["replies"] = []
    for rep in reply_objects:
      tmp_rep = {}
      tmp_rep["reply"] = rep.reply
      tmp_rep["id"] = rep.id
      tmp_rep["author"] = rep.author.username
      tmp_com["replies"]+=[tmp_rep]
    comment_list["comments"]+=[tmp_com]
  return JsonResponse(comment_list)

def register(request):
  if request.method == "POST":
    form_instance = forms.RegForm(request.POST)
    if form_instance.is_valid():
      form_instance.save()
      # user = form_instance.save()
      return redirect("/login/")
  else:
    form_instance = forms.RegForm()
  context = {
    "form":form_instance,
  }
  return render(request, "registration/register.html", context=context)

def api_home(request):
  SEARCH_API_URL = 'https://api.yelp.com/v3/businesses/search'
  API_KEY = 'KXfzN0UTapfsP7jWc9wlPoKpMPsbKFq_7TfdmnD0Ym0GDxvQNFEagIgPVyIanjpgFuEs3FoMYKTeZLnBjT7G6QzYniRpsASPBiOP2Gh0jd3eUxKgXsVQCtqn5fUnYnYx'
  HEADERS = {'Authorization': 'bearer %s' % API_KEY}
  PARAMETERS = {
    'location':'95926',
    'city':'Chico',
    'categories':'bars'
  }
  response=requests.get(url=SEARCH_API_URL, params=PARAMETERS, headers=HEADERS).json()
  total =  len(response['businesses'])
  for num in range(1, total+1):
    print(num)
  total_range = range(1, total+1)
  print(total)
  context = {
    'response':response,
    'total_range':total_range
  }
  return render(request, 'apihome.html', context=context)