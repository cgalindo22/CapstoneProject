from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import logout
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
import requests
from datetime import datetime, date

from . import models
from . import forms
from .ret_func import get_response



# home page-view
def index(request):
  context = {
    'response_q':get_response(),
  }
  return render(request, 'index.html', context=context)

class CreateProfile(CreateView):
  model = models.Profile
  form_class = forms.ProfilePageForm
  template_name = 'registration/create_profile.html'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ShowProfile(DetailView):
  model = models.Profile
  template_name = 'registration/profile.html'

  def get_profile(self, *args, **kwargs):
    users = model.Profile.objects.all()
    context = super(ShowProfile, self).get_profile(*args, **kwargs)
    page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
    context["page_user"] = page_user

    return context

class UserEditView(generic.UpdateView):
  form_class = forms.UpdateUserForm
  template_name = 'registration/edit_settings.html'
  success_url = reverse_lazy('plans')

  def get_object(self):
    return self.request.user

class EditProfileView(generic.UpdateView):
  form_class = forms.UpdateProfileForm
  # fields = ['avatar', 'bio']
  template_name = 'registration/edit_profile.html'
  success_url = reverse_lazy('plans')

  def get_object(self):
    return self.request.user

@login_required
def add_plan(request):
  if not request.user.is_authenticated:
    return redirect("/login/")
  if request.method == "POST":
    plan_form = forms.PlanForm(request.POST)
    if plan_form.is_valid():
      plan_form.save(request)
      return redirect("/plans/")      
  else:
    plan_form = forms.PlanForm()

  context = {
    'title':'Plan',
    'response_q':get_response(),
    'form':plan_form,
  }
  return render(request, 'add_plan.html', context=context)

def delete_plan(request, plan_id):
  plan = models.Plan.objects.filter(id=plan_id).delete()
  return redirect("/plans/")

@login_required
def plan_view(request):
  if request.method == "POST":
    if request.user.is_authenticated:
      plan_form = forms.PlanForm(request.POST)
      if plan_form.is_valid():
        plan_form.save(request)
        plan_form = forms.PlanForm()
  else:
    plan_form = forms.PlanForm()

  plan_objects = models.Plan.objects.all().order_by('date')
  plan_list =  []
  for plan in plan_objects:
    tmp_plan = {}
    tmp_plan["name"] = plan.name
    tmp_plan["title"] =  plan.title
    tmp_plan["date"] =  plan.date
    tmp_plan["time"] = plan.time
    tmp_plan["guests"] =  plan.guests
    tmp_plan["author"] = plan.author.username
    tmp_plan["id"] = plan.id
    plan_list+=[tmp_plan]

  context = {
      'plans':plan_list
    }
  return render(request, 'registration/plans.html', context=context)

def logout_view(request):
  logout(request)
  return redirect("/login/")

def register(request):
  if request.method == "POST":
    form_instance = forms.RegForm(request.POST)
    if form_instance.is_valid():
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



