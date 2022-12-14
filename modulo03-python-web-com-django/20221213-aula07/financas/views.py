from django.shortcuts import render

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

    return render(request, "financas/contas_por_usuario.html")
