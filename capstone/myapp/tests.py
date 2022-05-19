from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.

class BaseTest(TestCase):
  """ Test module for Profile model """
  def setUp(self):
    self.register_url = self.client.get('/register/')
    self.login_url = self.client.get('/login/')
    self.user = {
      'email':'galindosc20@gmail.com',
      'username':'sandoval1',
      'password1':'testingpassword',
      'password2':'testingpassword'
    }
    self.user_bad_password = {
      'email':'galindosc20@gmail.com',
      'username':'sandoval1',
      'password1':'test',
      'password2':'test'
    }
    self.user_unmatching_passwords = {
      'email':'galindosc20@gmail.com',
      'username':'sandoval1',
      'password1':'tests',
      'password2':'testss'
    }
    self.user_invalid_email = {
      'email':'galindo.gmail.com',
      'username':'sandoval1',
      'password1':'tests',
      'password2':'tests'
    }
    return super().setUp

class ViewsTestCase(BaseTest):
  def test_index_loads_properly(self):
      """The index page loads properly"""
      response = self.client.get('/')
      self.assertEqual(response.status_code, 200)

class ResgisterTest(BaseTest):
  def test_register_loads_properly(self):
    """The register page loads properly"""
    response = self.register_url
    self.assertEqual(response.status_code, 200)
    # self.assertTemplateUsed(response, 'registration/register.html')

  def test_can_register_user(self):
    response=self.client.post('/register/',self.user,format='text/html')
    self.assertEqual(response.status_code,302)

  def test_cant_register_user_withbadpassword(self):
    response=self.client.post(self.register_url,self.user_bad_password,format='text/html')
    self.assertEqual(response.status_code,400)

  def test_cant_register_user_with_unmatching_passwords(self):
    response=self.client.post(self.register_url,self.user_unmatching_passwords,format='text/html')
    self.assertEqual(response.status_code,400)
  
  def test_cant_register_user_with_invalid_email(self):
      response=self.client.post(self.register_url,self.user_invalid_email,format='text/html')
      self.assertEqual(response.status_code,400)

class LoginTest(BaseTest):
    def test_can_access_page(self):
        response=self.client.get('/login/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'registration/login.html')