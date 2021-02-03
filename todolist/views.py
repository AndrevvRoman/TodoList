from django.shortcuts import render, redirect #для отображения и редиректа берем необходимые классы
from django.http import HttpResponse
from .models import TodoList, User #не забываем наши модели

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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

# def login(request):
#     isLoggined = False
#     if request.method == "POST":
#         if "Login" in request.POST:
            
#             users = User.objects.all()
#             enteredMail = request.POST["mail"]
#             enteredPass = request.POST["password"]
#             for i in users:
#                 if i.mail == enteredMail and i.password == enteredPass:
#                     categories = Category.objects.all()
#                     print("Founded login in list")
#                     isLoggined = True
#                     return render(request, "category.html", {"categories": categories, "isLoggined" : isLoggined})
#             print("Didnt founded")
#     return render(request, "login.html", {"isLoggined" : isLoggined})

# def registrate(request):
#     if request.method == "POST":
#         if "Registrate" in request.POST:
#             users = User.objects.all()
#             enteredMail = request.POST["mail"]
#             enteredPass = request.POST["password"]
#             for i in users:
#                 if i.mail == enteredMail:
#                    return HttpResponse('<h1>Аккаунт уже существует</h1>')
#             login = User(mail=enteredMail,password=enteredPass)
#             login.save()
#             return redirect("/login")
#     return render(request, "registrate.html",{})

@login_required
def index(request):
    return render(request,"category.html")

def registrate(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,"category.html")
    context['form']=form
    return render(request,"registrate.html", context)