from django.urls import path

from . import views

urlpatterns = [
    #views.index→このアプリの中のapp.pyのindex関数を指定している
    path('', views.index, name='index'),
]