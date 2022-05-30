from django.urls import path
from .views import list_tasks,create_list,delete_task

urlpatterns=[
 path('',list_tasks),
 path('new/',create_list,name='create_task'),
 path('delete_task/<int:task_id>/',delete_task,name="delete_task"),
]