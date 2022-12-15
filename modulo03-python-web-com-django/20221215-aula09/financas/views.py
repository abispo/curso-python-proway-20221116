from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Transacao, ContaFinanceira


def index(request):

    num_transacoes = Transacao.objects.filter(
        conta_debito__usuario=request.user
    ).count()

    num_contas = ContaFinanceira.objects.filter(
        usuario=request.user
    ).count()

    context = {
        "num_transacoes": num_transacoes,
        "num_contas": num_contas
    }

    return render(
        request, "financas/index.html", context
    )


def transacoes_por_usuario(request, user_id):

    return render(request, "financas/transacoes_por_usuario.html")


def contas_por_usuario(request, user_id):
    todas_contas = ContaFinanceira.objects.filter(
        usuario=request.user
    )

    context = {
        "todas_contas": todas_contas
    }

    return render(
        request,
        "financas/contas_por_usuario.html",
        context
    )


def nova_conta(request, user_id):

    if request.method == "GET":
        return render(request, "financas/nova_conta.html")

    elif request.method == "POST":
        nome_nova_conta = request.POST.get("nome_conta")

        nova_conta = ContaFinanceira(
            usuario=request.user,
            nome=nome_nova_conta
        )
        nova_conta.save()

        return HttpResponseRedirect(
            reverse("financas:contas_por_usuario", args=(request.user.id,))
        )


def nova_transacao(request, user_id):

    contas_do_usuario = ContaFinanceira.objects.filter(
        usuario=request.user
    )

    if request.method == "GET":

        context = {
            "contas_do_usuario": contas_do_usuario
        }

        return render(
            request,
            "financas/nova_transacao.html",
            context
        )

    elif request.method == "POST":

        conta_debitada_id = int(request.POST.get("conta_debitada_id"))
        conta_creditada_id = int(request.POST.get("conta_creditada_id"))

        if conta_debitada_id == conta_creditada_id:
            context = {
                "erro": "Você não pode definir a mesma conta como débito e crédito",
                "contas_do_usuario": contas_do_usuario
            }

            return render(request, "financas/nova_transacao.html", context)

        valor_transacao = request.POST.get("valor_transacao")

        return HttpResponseRedirect(
            reverse("financas:transacoes_por_usuario", args=(request.user.id,))
        )
