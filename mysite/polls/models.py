from django.db import models

# Create your models here.
from django.db import models

class Question(models.Model):
    #ここの変数名はpythonで使うし、DBのカラム名になる
    question_text=models.CharField(max_length=200)
    #最初の位置引数は人間可読なフィールド名
    pub_date=models.DateTimeField('data published')

class Choice(models.Model):
    #リレーションシップを実現。それぞれのChoiceが一つのQuestionに関連付けられている
    question =models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text =models.CharField(max_length=200)
    votes=models.IntegerField(default=0)