from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myapp1(request):
  return HttpResponse('myhome welcome myapp1')