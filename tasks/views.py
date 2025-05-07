# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Geçici görev listesi (veritabanına geçtiğimiz için gerek yok ama kalsın istersen)
tasks = []

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        priority = request.POST.get("priority")
        Task.objects.create(title=title, priority=priority)
        return redirect("task_list")
    return render(request, "tasks/add_task.html")


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

# emre-backend: küçük düzenleme, görünürlük için eklendi
