from django.urls import path

from .views import index, transacoes_por_usuario

app_name = "financas"

urlpatterns = [
    path("", index, name="index"),
    path(
        "<int:user_id>/transacoes",
        transacoes_por_usuario,
        name="transacoes_por_usuario"
    )
]
