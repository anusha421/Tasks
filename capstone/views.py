from django.shortcuts import render
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .models import User, Task
import datetime


def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
    else:
        tasks = "Login to create a task."

    return render(request, "capstone/index.html", {
        "tasks": tasks
    })


def create(request):
    if request.method == "POST":
        body = request.POST.get('create-body')
        time = request.POST.get('create-time')
        task = Task.objects.create(
            user=request.user, body=body, task_date=time)
        task.save()
        return HttpResponseRedirect(reverse("index"))

    return render(request, 'capstone/create.html')


def complete(request, id):
    if Task.objects.filter(pk=id):
        task = Task.objects.get(pk=id)
    else:
        task = None

    if request.user.is_anonymous:
        return render(request, "capstone/index.html", {
            "message": "Login to create a task."
        })

    elif(task == None or task.user != request.user):
        return render(request, "capstone/index.html", {
            "message": "This is not a valid task."
        })

    else:
        if task.complete == False:
            task.complete = True
        else:
            task.complete = False
        task.completion_date = datetime.datetime.now()
        task.save(update_fields=['complete', 'completion_date', ])

    return HttpResponseRedirect(reverse("index"))


def task(request, id):
    if Task.objects.filter(pk=id):
        if Task.objects.get(pk=id).user == request.user:
            task = Task.objects.get(pk=id)
        else:
            task = None
    else:
        task = None

    return render(request, 'capstone/task.html', {
        "task": task
    })


def edit(request, id):
    if Task.objects.filter(pk=id):
        if Task.objects.get(pk=id).user == request.user and Task.objects.get(pk=id).complete == False:
            tasks = Task.objects.get(pk=id)
        else:
            tasks = None
    else:
        tasks = None

    if request.method == 'POST':
        body = request.POST.get('edit-body')
        time = request.POST.get('edit-time')
        tasks.body = body
        tasks.task_date = time
        tasks.save(update_fields=['body', 'task_date',])
        return task(request, tasks.id)

    return render(request, 'capstone/edit.html', {
        "task": tasks
    })


def delete(request, id):
    if request.user.is_authenticated:
        if Task.objects.filter(pk=id):
            task = Task.objects.get(pk=id)
            if task.user == request.user:
                task.delete()
            else:
                return render(request, "capstone/index.html", {
                    "message": "This is not a valid task."
                })
        else:
            return render(request, "capstone/index.html", {
                "message": "This is not a valid task."
            })
    else:
        return render(request, "capstone/index.html", {
            "message": "Login to create a task."
        })

    return HttpResponseRedirect(reverse("index"))


def search(request):
    if request.user.is_authenticated:
        search_input = request.GET.get("q")
        tasks = Task.objects.filter(user=request.user)
        for each_task in tasks:
            if search_input == each_task.body:
                return task(request, each_task.id)

        return render(request, "capstone/search.html", {
            "input": search_input,
            "tasks": tasks
        })
    else:
        return render(request, "capstone/index.html", {
            "message": "Login to view."
        })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "capstone/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "capstone/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "capstone/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "capstone/register.html", {
                "message": "Username already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "capstone/register.html")
