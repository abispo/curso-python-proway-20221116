from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from polls.models import Question, Choice


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

    context = {
        "question": question
    }
    return render(request, "polls/detail.html", context)


def results(request, question_id):
    return HttpResponse(f"Você está vendo os resultados da pergunta {question_id}.")


def vote(request, question_id):

    # Carregamos um objeto Question da tabela tb_questions, a partir do question_id
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Abaixo tentamos carregar um objeto choice a partir do valor da opção choice que vem
        # do formulário. 'choice' é o nome dos elementos radio button no formulário. Aqui
        # receberemos o valor que estiver em 'value'
        # POST é um dicionários com os campos que foram enviados de um formulário utilizando o
        # método POST
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "Você não escolheu uma opção para votar"
        }
        return render(request, "polls/detail.html", context)

    else:
        # Incrementamos a quantidade de votos da opção selecionada em 1
        selected_choice.votes += 1

        # Salvamos (atualizamos) o objeto com a nova quantidade de votos
        selected_choice.save()


        # Por boas práticas, sempre que um usuário enviar dados via POST, redirecionamos o usuário
        # para outra página, por isso utilizamos o HttpResponseRedirect
        # A função reverse gera a URL a partir do nome da rota. Se essa rota precisar receber
        # algum tipo de parâmetro, passamos pelo argumento args

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
