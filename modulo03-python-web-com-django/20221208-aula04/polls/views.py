from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from polls.models import Question


# function-based view
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")

    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # get_object_or_404 retorna um objeto caso exista. Se não existir, gera
    # um erro 404
    question = get_object_or_404(Question, pk=question_id)

    # primary key -> chave primária
    # question = Question.objects.get(pk=question_id)

    context = {"question": question}
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    return HttpResponse(f"Você está vendo os resultados da pergunta {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"Você está votando na pergunta {question_id}.")
