"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from todolist.views import todo
from todolist.views import sign_in
from todolist.views import registrate
from todolist.views import redirect_view
from todolist.views import sign_out

urlpatterns = [
	url(r'$^', redirect_view ),
	url(r'^admin/', admin.site.urls),
	url(r'^todo/', todo, name="todo"),
# 	url(r'^category/', category, name="Category"),
    url(r'^sign_in/', sign_in, name="sign_in"),
    url(r'^sign_out/', sign_out, name="sign_out"),
    url(r'^registrate/', registrate, name="registrate"),
]

# urlpatterns = [
#     # path('',todolist.views.index,name="home"),
#     path('registrate/',registrate,name="registrate")
# ]