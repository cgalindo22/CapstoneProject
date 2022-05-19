from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('', views.index),
  path('login/', auth_views.LoginView.as_view()),
  path('register/', views.register),
  path('logout/', views.logout_view),
  path('comments/', views.get_comments),
  path('test/', views.comment_test),
  path('plans/', views.plan_view, name='plans'),
  path('settings/', views.UserEditView.as_view(), name='edit-settings'),
  path('<int:pk>/profile/', views.ShowProfile.as_view(), name='showprofile'),
  path('<int:pk>/edit_profile/', views.EditProfileView.as_view(), name="edit-profile"),
  path('create_profile/', views.CreateProfile.as_view(), name="create-profile"),
  path('add_plan/', views.add_plan),
  path('delete_plan/<int:plan_id>', views.delete_plan, name='delete-plan'),
]