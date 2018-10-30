from django.urls import path, reverse
from . import views

app_name = 'tasks'

urlpatterns = [
    path('',views.index,name='index'),
    path('add/', views.TaskCreate.as_view(), name='task-add'),
    path('<slug:pk>/edit/',views.TaskUpdate.as_view(),name='task_edit'),
    path('<slug:pk>/done/', views.task_done, name='task_done'),
    path('<slug:pk>/undone/', views.task_undone, name='task_undone'),
    path('<slug:pk>/delete/', views.task_delete, name='task_delete'),
    path('?dateselect=<str:date>',views.task_date,name="jump_to"),
    path('<str:date>/',views.task_date,name="task_date"),
    path('reports',views.report,name='report'),
    path('labels',views.labels,name='labels'),
    path('labels/add',views.LabelCreate.as_view(),name='label_add'),
    path('labels/<slug:pk>/edit/',views.LabelUpdate.as_view(),name='label_edit'),
    path('labels/<slug:pk>/delete/',views.label_delete,name='label_delete'),
    path('settings',views.settings,name='settings'),
    path('whatsnew',views.whatsnew,name='whatsnew'),
    path('about', views.about, name='about')
]
