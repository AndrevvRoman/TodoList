from django.utils import timezone #мы будем получать дату создания todo
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True) #текстовое поле
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # дата создания
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) #до какой даты нужно было сделать дело
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta: #используем вспомогательный класс мета для сортировки наших дел
        ordering = ["-created"] #сортировка дел по времени их создания
    def __str__(self):
        return self.title