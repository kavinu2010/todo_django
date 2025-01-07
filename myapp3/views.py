from django.shortcuts import render 
from django.views.generic.list import ListView 
from .models import CreateTask
 
# Create your views here.
class CreateTask(ListView):
  model=CreateTask
  context_object_name='tasks'
