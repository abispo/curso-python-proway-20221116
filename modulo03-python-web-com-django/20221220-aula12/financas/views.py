
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import Q

from .models import Transacao, ContaFinanceira


@login_required
def index(request):

    return render(request, "financas/index.html")

@login_required
def transacoes_por_usuario(request):

    todas_transacoes = Transacao.objects.filter(
        conta_debito__usuario=request.user
    )

    context = {
        "todas_transacoes": todas_transacoes
    }

    return render(
        request,
        "financas/transacoes_por_usuario.html",
        context
    )


@login_required
def contas_por_usuario(request):
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


@login_required
def nova_conta(request):

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
            reverse("financas:contas_por_usuario")
        )


@login_required
def nova_transacao(request):

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
        valor_transacao = valor_transacao.replace(",", ".")
        valor_transacao = float(valor_transacao)

        conta_debitada = ContaFinanceira.objects.get(pk=conta_debitada_id)
        conta_creditada = ContaFinanceira.objects.get(pk=conta_creditada_id)

        conta_debitada.saldo -= valor_transacao
        conta_creditada.saldo += valor_transacao

        transacao = Transacao(
            conta_debito=conta_debitada,
            conta_credito=conta_creditada,
            valor=valor_transacao
        )

        transacao.save()
        conta_debitada.save()
        conta_creditada.save()

        return HttpResponseRedirect(
            reverse("financas:transacoes_por_usuario")
        )


@login_required
def detalhe_conta(request, conta_id):

    conta = ContaFinanceira.objects.get(pk=conta_id)

    if conta.usuario != request.user:
        return HttpResponse("Você não tem acesso a essa página", status=401)

    transacoes = Transacao.objects.filter(
        Q(conta_debito=conta) | Q(conta_credito=conta)
    )

    context = {
        "conta": conta,
        "transacoes": transacoes
    }

    return render(
        request,
        "financas/detalhe_conta.html",
        context
    )


@login_required
def perfil_usuario(request):

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

    return render(request, "financas/perfil_usuario.html", context)


@login_required
def editar_conta(request, conta_id):

    conta = get_object_or_404(ContaFinanceira, pk=conta_id)

    if request.method == "GET":
        return render(request, "financas/editar_conta.html", {"conta": conta})

    elif request.method == "POST":

        nome_conta = request.POST.get("nome_conta", conta.nome)
        conta.nome = nome_conta
        conta.save()

        return HttpResponseRedirect(reverse("financas:detalhe_conta", args=(conta.id,)))


def criar_usuario(request):

    return render(request, "financas/criar_usuario.html")
