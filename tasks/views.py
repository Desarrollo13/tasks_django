import re
from turtle import title
from urllib import request
from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def list_tasks(request):
    tasks=Task.objects.all()   
    return render(request, "list_tasks.html",{'tasks':tasks})

def create_list(resquest):
   tasks=Task(title=resquest.POST['title'],description=resquest.POST['description'])
   tasks.save()
   return redirect('/tasks/')

# creo una vista especial para elminar
def delete_task(request,task_id):
   tasks=Task.objects.get(id=task_id)
   tasks.delete()
   return redirect('/tasks/')

