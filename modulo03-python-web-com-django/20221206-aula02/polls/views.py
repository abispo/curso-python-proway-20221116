from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Question


# function-based view
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")

    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    return HttpResponse(f"Você está vendo os detalhes da pergunta {question_id}.")


def results(request, question_id):
    return HttpResponse(f"Você está vendo os resultados da pergunta {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"Você está votando na pergunta {question_id}.")
