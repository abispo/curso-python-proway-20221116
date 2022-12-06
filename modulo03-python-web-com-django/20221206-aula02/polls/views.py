from django.shortcuts import render
from django.http import HttpResponse

# function-based view
def index(request):
    return HttpResponse("Olá mundo! Página index do polls app.")
