from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect

from django.urls import reverse
from django.views import generic

from .models import Question,choice

# Create your views here.

class IndexView(generic.ListView):
	template_name='polls/index.html'
	context_object_name='list_question'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model=Question
	template_name='polls/detail.html'

class ResultView(generic.DetailView):
	model=Question
	template_name='polls/results.html'


def vote(request,question_id):
	question=get_object_or_404(Question,pk=question_id)
	try:
		select_choice=question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,choice.DoesNotExists):
		return render(request,'polls/detail.html',{
			'question':question,
			'error_message':"You Didn't Select a Choice",
		})

	else:
		select_choice.votes+=1;
		select_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))























