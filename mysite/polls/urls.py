from django.urls import path

from . import views

urlpatterns = [
    #name引数のおかげで.htmlファイルに検索をかけることができる
    #views.index→このアプリの中のview.pyのindex関数を指定している
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]