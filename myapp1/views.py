
from django.views.generic.list import ListView
from .models import Todo_task


# Create your views here.
class Task_List(ListView):
  model=Todo_task
  context_object_name='tasks'