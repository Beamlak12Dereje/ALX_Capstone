from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.db.models import Q
from datetime import datetime

@login_required
def task_list(request):
    status = request.GET.get('status')
    date_filter = request.GET.get('date')
    tasks = Task.objects.filter(owner=request.user)
    if status == 'completed':
        tasks = tasks.filter(is_completed=True)
    elif status == 'incomplete':
        tasks = tasks.filter(is_completed=False)
    if date_filter:
        try:
            due_date = datetime.strptime(date_filter, '%Y-%m-%d')
            tasks = tasks.filter(due_date__date=due_date.date())
        except ValueError:
            pass  # Invalid date, ignore
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_edit(request, id):
    task = get_object_or_404(Task, id=id, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def task_delete(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id, owner=request.user)
        task.delete()
    return redirect('task_list')

@login_required
def task_toggle(request, id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=id, owner=request.user)
        task.is_completed = not task.is_completed
        task.save()
    return redirect('task_list')