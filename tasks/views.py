# tasks/views.py

from django.shortcuts import render, redirect

# Geçici görev listesi
tasks = []

def task_list(request):
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        priority = request.POST['priority']
        tasks.append({'title': title, 'priority': priority})
        return redirect('task_list')
    return render(request, 'tasks/add_task.html')
