from django.shortcuts import render, redirect #для отображения и редиректа берем необходимые классы
from django.http import HttpResponse
from .models import Todo #не забываем наши модели

from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
 
def redirect_view(request):
	return redirect("/registrate") # редирект с главной на категории

def todo(request):
    todos = TodoList.objects.all() #запрашиваем все объекты todo через менеджер объектов
    categories = Category.objects.all() #так же получаем все Категории

    if request.method == "POST": #проверяем то что метод именно POST
        if "Add" in request.POST: #проверяем метод добавления todo
            title = request.POST["description"] #сам текст
            date = str(request.POST["date"]) #дата, до которой должно быть закончено дело
            category = request.POST["category_select"] #категория, которой может выбрать или создать пользователь.
            content = title + " -- " + date + " " + category # полный склеенный контент
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() # сохранение нашего дела
            return redirect("/todo") # перегрузка страницы (ну вот так у нас будет устроено очищение формы)
        if "Delete" in request.POST: #если пользователь собирается удалить одно дело
            checkedlist = request.POST.getlist('checkedbox') # берем список выделенные дел, которые мы собираемся удалить
            for i in range(len(checkedlist)): #мне почему-то не нравится эта конструкция
                todo = TodoList.objects.filter(id=int(checkedlist[i]))
                todo.delete() #удаление дела
    return render(request, "todo.html", {"todos": todos, "categories": categories})

def sign_in(request):
    if request.method == "POST":
        if "Login" in request.POST:
            enteredUsername = request.POST["username"]
            enteredPass = request.POST["password"]
            user = authenticate(request, username=enteredUsername, password=enteredPass)
            if user is not None:
                login(request,user)
                return render(request, "todo.html", {"todos" : Todo.objects.filter(owner=user)})
    return render(request, "sign_in.html", {"hasError" : True})

@login_required
def index(request):
    return render(request,"category.html")

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