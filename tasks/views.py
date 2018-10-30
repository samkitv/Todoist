from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Task,Label
import datetime, calendar

def index(request):
    date=datetime.date.today()
    done_tasks=Task.objects.filter(date=date,Done=True)
    rem_tasks=Task.objects.filter(date=date,Done=False)
    return render(request, 'tasks/index.html', {'done_tasks':done_tasks,'rem_tasks':rem_tasks,'date':date,'day':calendar.day_name[date.weekday()]})

def task_date(request,date):
    done_tasks = Task.objects.filter(date=date, Done=True)
    rem_tasks = Task.objects.filter(date=date, Done=False)
    return render(request, 'tasks/index.html', {'done_tasks': done_tasks, 'rem_tasks': rem_tasks, 'date': datetime.datetime.strptime(date,'%Y-%m-%d').date(),
                                                'day': calendar.day_name[datetime.datetime.fromisoformat(date).weekday()]})

def task_done(request,pk):
    task=Task.objects.get(id=pk)
    task.Done=True
    task.save()
    return redirect('tasks:task_date', task.date)

def task_undone(request,pk):
    task=Task.objects.get(id=pk)
    task.Done=False
    task.save()
    return redirect('tasks:task_date', task.date)

class TaskCreate (CreateView):
    model = Task
    fields = ['name','date','time','label','points','isBonus']
    def get_success_url(self):
        return reverse('tasks:index')

class TaskUpdate (UpdateView):
    model = Task
    fields = ['name','date','time','label','points','isBonus']
    def get_success_url(self):
        return reverse('tasks:index')

def task_delete(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect('tasks:task_date',task.date)

def report(request):
    dates=Task.objects.values_list('date',flat=True).distinct().order_by('date').reverse()
    l=tuple()
    rep=tuple()
    for date in dates:
        norm_points=Task.objects.filter(date=date, isBonus=False, Done= True).aggregate(Sum('points'))
        bonus_points=Task.objects.filter(date=date, isBonus=True, Done= True).aggregate(Sum('points'))
        tot_points=Task.objects.filter(date=date, Done= True).aggregate(Sum('points'))
        l=(date,norm_points,bonus_points,tot_points)
        rep = rep + (l,)
    return render(request, 'tasks/reports.html', {'rep':rep})


def labels(request):
    labels=Label.objects.all()
    return render(request,'tasks/labels.html',{'labels':labels})

class LabelCreate (CreateView):
    model = Label
    fields = ['name']
    def get_success_url(self):
        return reverse('tasks:labels')

class LabelUpdate (UpdateView):
    model = Label
    fields = ['name']
    def get_success_url(self):
        return reverse('tasks:labels')

def label_delete(request,pk):
    label=Label.objects.get(id=pk)
    label.delete()
    return redirect('tasks:labels')

def settings(request):
    return render(request,'tasks/settings.html')

def whatsnew(request):
    return render(request,'tasks/whatsnew.html')

def about(request):
    return render(request,'tasks/about.html')
