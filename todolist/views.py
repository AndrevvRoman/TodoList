from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import Todo 
 
def redirect_view(request):
	return redirect("/sign_in")

@login_required
def todo(request):
    todos = Todo.objects.filter(owner=request.user)
    print("todo")
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
                todo.delete()
    if request.method == "GET":
        if "sign_out" in request.GET:
            logout(request)
            return redirect('sign_in')
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
    return render(request, "sign_in.html", {"hasError" : False})

@login_required
def sign_out(request):
    logout(request)
    return redirect('/sign_in')

def registrate(request):
    context = {}
    if request.method == "POST":
        if "SignUp" in request.POST:
            enteredMail = request.POST["mail"]
            enteredUsername = request.POST["username"]
            enteredPass1 = request.POST["password1"]
            enteredPass2 = request.POST["password1"]
            try:
                if enteredPass1 != enteredPass2:
                    print("pass exep")
                    raise ValueError("Password entered incorrectly!")
                if User.objects.filter(email=enteredMail).exists():
                    print("email exep")
                    raise ValueError("Email already exsists!")
                if User.objects.filter(username=enteredUsername).exists():
                    print("email exep")
                    raise ValueError("Nickname already exsists!")
            except ValueError as er:
                print("cathed exep")
                context["hasError"] = True
                context["errorText"] = str(er)
                return render(request,"registrate.html", context)

            print("Creating new user")
            newUser = User.objects.create_user(enteredUsername, enteredMail, enteredPass1)
            newUser.save()
            return redirect('/sign_in')
    if request.method == "GET":
        if "DeleteError" in request.POST:
            context["hasError"] = False
            context["errorText"] = ""
    return render(request,"registrate.html", context)