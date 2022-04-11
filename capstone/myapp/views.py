from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from gql.transport.requests import RequestsHTTPTransport
from gql import gql, Client
from datetime import datetime
import calendar
import requests

from . import models
from . import forms


# API constants
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash
API_KEY = 'KXfzN0UTapfsP7jWc9wlPoKpMPsbKFq_7TfdmnD0Ym0GDxvQNFEagIgPVyIanjpgFuEs3FoMYKTeZLnBjT7G6QzYniRpsASPBiOP2Gh0jd3eUxKgXsVQCtqn5fUnYnYx' # YELP API Bearer key

# home page-view
def index(request):
  HEADER = {'Authorization': 'bearer %s' % API_KEY}
  # Build the request framework
  transport = RequestsHTTPTransport(url='https://api.yelp.com/v3/graphql', headers=HEADER, use_json=True)
  # Create the client
  client = Client(transport=transport, fetch_schema_from_transport=True)
  # define a simple query
  query = gql(''' 
  {
    search(term:"downtown",
         location:"Chico, 95928",
  				categories:"restaurants") {
      total
      business {
        name
        hours {
          is_open_now
          open {
            start
            end
            day
          }
        }
        rating
        price
        location {
          formatted_address
        }
        display_phone
      }
    }
  }
  ''')
  response_q = client.execute(query)
  for i in range(0,20):
    # print(i)
    if response_q['search']['business'][i]['hours']:
      start_hours = response_q['search']['business'][i]['hours'][0]['open'] # change [] before start to have 1-4 or however many values
      for c, start in enumerate(start_hours):
        change_start = datetime.strptime(start['start'], '%H%M').strftime('%I:%M %p')
        change_end = datetime.strptime(start['end'], '%H%M').strftime('%I:%M %p')
        change_day = calendar.day_name[start['day']]
        response_q['search']['business'][i]['hours'][0]['open'][c]['start'] = change_start
        response_q['search']['business'][i]['hours'][0]['open'][c]['end'] = change_end
        response_q['search']['business'][i]['hours'][0]['open'][c]['day'] = change_day
  # testing 
  # print(response_q['search']['business'][1]['hours'][0]['open'][0])
  context = {
    'response_q':response_q['search']['business'][0:20],
  }
  return render(request, 'index.html', context=context)

class UserEditView(generic.UpdateView):
  form_class = forms.UpdateProfileForm
  template_name = 'registration/edit_profile.html'
  success_url = reverse_lazy('profile')

  def get_object(self):
    return self.request.user

@login_required
def profile(request):
  # if request.method == 'POST':
  #   user_form = forms.UpdateUserForm(request.POST, instance=request.user)
  #   profile_form = forms.UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

  #   if user_form.is_valid() and profile_form.is_valid():
  #     user_form.save()
  #     profile_form.save()
  #     messages.success(request, 'Your profile is updated successfully')
  #     return redirect(to='users-profile')
  # else:
  #     user_form = forms.UpdateUserForm(instance=request.user)
  #     profile_form = forms.UpdateProfileForm(instance=request.user.profile)

  context = {
    # 'user_form': user_form, 
    # 'profile_form': profile_form
    }

  return render(request, 'profile.html', context=context)

def logout_view(request):
  logout(request)
  return redirect("/login/")


def register(request):
  if request.method == "POST":
    form_instance = forms.RegForm(request.POST)
    if form_instance.is_valid():
      # form_instance.save()
      user = form_instance.save()
      return redirect("/login/")
  else:
    form_instance = forms.RegForm()
  context = {
    "form":form_instance,
  }
  return render(request, "registration/register.html", context=context)

def comment_test(request):
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
  return render(request, "comment_test.html", context=context)

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



