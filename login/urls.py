from django.urls import path
from login.views import *
 
app_name = 'login'

urlpatterns = [
    path('',Login, name='login'),
]