# tasks/views.py

from django.shortcuts import render, redirect
from .models import Task


# Geçici görev listesi
tasks = []

def task_list(request):
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        priority = request.POST.get("priority")
        Task.objects.create(title=title, priority=priority)
        return redirect("task_list")
    return render(request, "tasks/add_task.html")