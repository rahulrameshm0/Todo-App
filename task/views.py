from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from . models import Task
# Create your views here.
def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task')
        
        messages.error(request,"username or password is incorrect")
        return redirect('login')

    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
    
        if User.objects.filter(username=username).exists():
            messages.error(request, 'This username already exists')
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "This email address already exists")
            return redirect('signup')
        
        if password != confirm_password:
            messages.error(request, 'password does not match!')
            return redirect('signup')
        
        create_account = User.objects.create_user(username=username,email=email,password=password)
        create_account.save()
        return render(request, 'login.html')

    return render(request, 'signup.html')

def signout(request):
    logout(request)
    return redirect('login')

def task(request):
    # task = Task.objects.all()
    # return render(request, 'todo.html', {"details":task})
    tasks = Task.objects.filter(task_complete=False)
    completed = Task.objects.filter(task_complete=True)
    return render(request, 'todo.html', {'tasks': tasks, 'completed': completed})

def add_list(request):
    if request.method == "POST":
        task = request.POST['task']
        priority = request.POST['priority']
        due_date = request.POST['date']

        new_task = Task(task=task,priority=priority,date=due_date)
        new_task.save()
        return redirect('task')
    
def edit(request, id):
    t = get_object_or_404(Task,id=id)
    if request.method == "POST":
        task_name = request.POST['task']
        priority = request.POST['priority']
        date = request.POST['date']
        t.task = task_name
        t.priority=priority
        t.date=date
        t.save()
        return redirect('task')
    return render(request, 'update.html', {'edits':t})


def deleteform(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task')


def high_priority(request):
    data = Task.objects.filter(priority='High')
    return render(request, 'todo.html',{'tasks':data})

def medium_priority(request):
    data = Task.objects.filter(priority='Medium')
    return render(request, 'todo.html',{'tasks':data})


def low_priority(request):
    data = Task.objects.filter(priority='Low')
    return render(request, 'todo.html',{'tasks':data})


def mark_completed(request, id):
    task = get_object_or_404(Task, id=id)
    # print(f"Marked task {task.task} as complete")
    task.task_complete = True
    task.save()
    return redirect('task')

def unmark_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.task_complete = False
    task.save()
    return redirect('task')