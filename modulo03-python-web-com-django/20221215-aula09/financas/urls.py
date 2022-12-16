from django.urls import path

from .views import (
    index,
    transacoes_por_usuario,
    contas_por_usuario,
    nova_conta,
    nova_transacao,
    detalhe_conta
)

app_name = "financas"

urlpatterns = [
    path("", index, name="index"),
    path(
        "<int:user_id>/transacoes",
        transacoes_por_usuario,
        name="transacoes_por_usuario"
    ),
    path(
        "<int:user_id>/contas",
        contas_por_usuario,
        name="contas_por_usuario"
    ),
    path(
        "<int:user_id>/contas/nova",
        nova_conta,
        name="nova_conta"
    ),
    path(
        "<int:user_id>/transacoes/nova",
        nova_transacao,
        name="nova_transacao"
    ),
    path(
        "<int:user_id>/contas/<int:conta_id>",
        detalhe_conta,
        name="detalhe_conta"
    )
]
