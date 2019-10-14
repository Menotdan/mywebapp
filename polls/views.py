from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from .models import Choice,Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def question_results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    template = loader.get_template('polls/question_results.html')
    context = {
        'question': question,
        'question_id': question_id,
    }
    return HttpResponse(template.render(context, request))

def question_vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/question_details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:question_results', args=(question.id,)))


def question_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    template = loader.get_template('polls/question_details.html')
    context = {
        'question': question,
    }
    return HttpResponse(template.render(context, request))
