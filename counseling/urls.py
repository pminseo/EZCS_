from django.urls import path 
from . import views

app_name = 'counseling'

urlpatterns = [
    path('', views.list, name='list'),
]
