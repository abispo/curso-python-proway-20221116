from django.urls import path

# import relativo
# A partir da pasta onde o arquivo está, import o módulo views
from . import views

urlpatterns = [
    path("", views.index, name="index")
]
