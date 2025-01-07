from django.urls import path

from .views import Task_List

urlpatterns=[
  path('home/',Task_List.as_view(),name='home' )
]