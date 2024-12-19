from django.shortcuts import render, redirect
from app.models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url="login")
def main_view(request):
    return render(request, "main.html")


@login_required(login_url="login")
def tasks_api_view(request):
    if request.method == "POST":
        Task.objects.create(description=request.POST["description"], user=request.user)
    tasks = Task.objects.filter(user=request.user)
    return render(request, "tasks.html", {"data": tasks})


@login_required(login_url="login")
def task_api_delete(request, pk):
    Task.objects.filter(pk=pk, user=request.user).delete()
    return redirect("tasks")


@login_required(login_url="login")
def task_api_complete(request, pk):
    try:
        task = Task.objects.get(pk=pk, user=request.user)
        task.is_done = not task.is_done
        task.save()
    except Task.DoesNotExist:
        pass
    return redirect("tasks")


def registration_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration.html", {"form": form})


def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            error = "Неверный логин или пароль"

    return render(request, "login.html", {"error": error})


def logout_view(request):
    logout(request)
    return redirect("login")
