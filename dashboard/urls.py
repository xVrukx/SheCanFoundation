from django.urls import path
from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('leaderboard/', leaderboard, name='leaderboard')
]