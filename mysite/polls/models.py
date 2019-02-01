from django.db import models
import datetime
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    #ここの変数名はpythonで使うし、DBのカラム名になる
    question_text=models.CharField(max_length=200)
    #最初の位置引数は人間可読なフィールド名
    pub_date=models.DateTimeField('data published')
    #どんな内容を追加したか、確認できるためのメソッド
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >=timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
    #リレーションシップを実現。それぞれのChoiceが一つのQuestionに関連付けられている
    question =models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text =models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text