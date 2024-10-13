from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'AniKans',
        'content': 'Работа с БД',
    }
    return render(request, 'main/index.html', context)
