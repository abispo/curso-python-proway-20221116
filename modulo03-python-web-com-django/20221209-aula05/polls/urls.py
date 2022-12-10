from django.urls import path

# import relativo
# A partir da pasta onde o arquivo está, import o módulo views
from .views import index, detail, results, vote, statistics, comment
# namespace
app_name = "polls"

urlpatterns = [
    path("", index, name="index"),
    # question_id é um parâmetro passado via URL
    # Ou seja, ele pode mudar a qualquer chamada
    path("<int:question_id>/", detail, name="detail"),
    path("<int:question_id>/results/", results, name="results"),
    path("<int:question_id>/vote/", vote, name="vote"),
    path("<int:question_id>/comment/", comment, name="comment"),
    path("statistics/", statistics, name="statistics")
]
