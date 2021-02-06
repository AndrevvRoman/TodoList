from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from .models import Todo 
 
def redirect_view(request):
	return redirect("/sign_in")

def todo(request):
    todos = Todo.objects.filter(owner=request.user)

    if request.method == "POST":
        if "Add" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            content = title + " -- " + date + " " # полный склеенный контент
            newTodo = Todo(title=title, content=content, due_date=date, owner=request.user)
            newTodo.save()
            return redirect("/todo")
        if "Delete" in request.POST: #если пользователь собирается удалить одно дело
            checkedlist = request.POST.getlist('checkedbox') # берем список выделенные дел, которые мы собираемся удалить
            for i in range(len(checkedlist)):
                todo = Todo.objects.filter(id=int(checkedlist[i]))
                todo.delete() #удаление дела
    return render(request, "todo.html", {"todos": todos})

def sign_in(request):
    if request.method == "POST":
        if "Login" in request.POST:
            enteredUsername = request.POST["username"]
            enteredPass = request.POST["password"]
            user = authenticate(request, username=enteredUsername, password=enteredPass)
            if user is not None:
                login(request,user)
                todos = Todo.objects.filter(owner=request.user)
                return redirect('/todo')
                # return redirect(reverse('todo.html',{"todos" : Todo.objects.filter(owner=user)}))
                # return render(request, "todo.html", {"todos" : Todo.objects.filter(owner=user)})
    return render(request, "sign_in.html", {"hasError" : False})

def registrate(request):
    context = {}
    if request.method == "POST":
        enteredMail = request.POST["mail"]
        enteredUsername = request.POST["username"]
        enteredPass1 = request.POST["password1"]
        enteredPass2 = request.POST["password1"]
        if enteredPass1 == enteredPass2 and not User.objects.filter(email=enteredMail).exists():
            print("Creating new user")
            newUser = User.objects.create_user(enteredUsername, enteredMail, enteredPass1)
            newUser.save()
            return render(request,"sign_in.html", context)
        else:
            context["hasError"] = True
    return render(request,"registrate.html", context)