from django.urls import path

from .views import (
    index,
    transacoes_por_usuario,
    contas_por_usuario,
    nova_conta,
    nova_transacao,
    detalhe_conta,
    perfil_usuario
)

app_name = "financas"

urlpatterns = [
    path("", index, name="index"),
    path(
        "transacoes/",
        transacoes_por_usuario,
        name="transacoes_por_usuario"
    ),
    path(
        "contas/",
        contas_por_usuario,
        name="contas_por_usuario"
    ),
    path(
        "contas/nova/",
        nova_conta,
        name="nova_conta"
    ),
    path(
        "transacoes/nova/",
        nova_transacao,
        name="nova_transacao"
    ),
    path(
        "contas/<int:conta_id>/",
        detalhe_conta,
        name="detalhe_conta"
    ),
    path(
        "perfil/",
        perfil_usuario,
        name="perfil_usuario"
    ),
]
