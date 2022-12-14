from django.urls import path

from .views import index, transacoes_por_usuario, contas_por_usuario

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
    )
]
