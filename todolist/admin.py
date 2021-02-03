from django.contrib import admin

from .models import TodoList, User

# admin.site.register(Category)
admin.site.register(TodoList)
admin.site.register(User)
