from pyexpat import model
from statistics import mode
from turtle import update
from venv import create
from django.db import models

# Create your models here.
class Task(models.Model):
   title=models.CharField(max_length=100)
   description=models.TextField(blank=True)
 