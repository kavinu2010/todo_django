from django.db import models

# Create your models here.
class Todo_task(models):
   user=models.ForeignKey(User, on_delete=models.CASCADE)