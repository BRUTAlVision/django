from django.shortcuts import render, redirect
from todo.models import Task

def home(request):
    tasks_not_completed = Task.objects.filter(is_completed=False).order_by('created_at')
    tasks_completed = Task.objects.filter(is_completed=True).order_by('created_at')
    context = { 
        'tasks_not_completed': tasks_not_completed,
        'tasks_completed': tasks_completed,
    }
    return render(request, 'home.html', context)

def add_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        if task_name:
            Task.objects.create(task=task_name, is_completed=False)
    return redirect('home')