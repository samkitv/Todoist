from django.db import models
from datetime import date,time
from django.urls import reverse

# Create your models here.


class Task(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField(default=date.today,null=True,blank=True)
    time=models.TimeField(auto_now=False,null=True,blank=True)
    label=models.ForeignKey('Label',on_delete=models.SET_NULL,null=True,blank=True)
    points=models.PositiveIntegerField(default=1000)
    isBonus=models.BooleanField(default=False)
    Done=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('tasks:task_edit', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name + ' (' + str(self.date) + ')'

class Label(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name