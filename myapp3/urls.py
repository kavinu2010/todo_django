from django.urls import path
from .views import CreateTask

urlpatterns=[
  path('home3/', CreateTask.as_view(),name='home3'),
]