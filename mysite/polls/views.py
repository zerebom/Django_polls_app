from django.shortcuts import render,get_object_or_404
from django.http import Http404,HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# from django.template import loader
#root ディレクトリからみて.でimportできる
from .models import Choice,Question
from django.views import generic

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     # try:
#     #     question=Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exist')
#     # return render(request, 'polls/detail.html',{'question':question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})



#オブジェクトのリストを表示する
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

#あるタイプのオブジェクトの詳細ページを表示する
#question_idをpkに変更している
#template_name属性を指定すると指定されたテンプレート名を使うようになる
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

#DetailViewのサブクラスのなので仕組みはうえと同じ
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        #postデータを受け取っている↓
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    #なければ、KeyErrorを送出する。
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.ポストデータが成功したときは、二重で返したりしない様にredirectを使う
        #reverse()を呼ぶと、その関数でビューに与える、位置引数と名前を渡す。（？ハードコーディングを防げる）
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))