from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:id>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:id>/toggle/', views.task_toggle, name='task_toggle'),
]