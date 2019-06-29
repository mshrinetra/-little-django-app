from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.template import loader
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

# # Common View
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}

#     # # Vanila Method
#     # template = loader.get_template('polls/index.html')
#     # return HttpResponse(template.render(context, request))

#     # Shortcut Method
#     return render(request, 'polls/index.html', context)


# def details(request, question_id):
#     # # Vanila Method
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist as onject_not_found:
#     #     raise Http404("Question with id {} not found!!".format(question_id))
#     # return HttpResponse("Welcome to details for Question {}".format(question_id))

#     # Shortcut Method
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'polls/details.html', context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'polls/results.html', context)


# GenericView

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailsView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    if request.POST:
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(
                pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist, NameError) as choice_error:
            return render(request, 'polls/details.html', {
                'question': question,
                'error_message': 'You did not selected a correct option!'
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    else:
        return HttpResponseForbidden()
