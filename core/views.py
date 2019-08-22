from django.shortcuts import render

# Create your views here.
from core.models import Evento


def home(request):
    contexto = {}
    return render(request,
                  'index.html',
                  contexto)


def eventos(request):
    eventos = Evento.objects.all()
    myeventos = []
    for evento in eventos:
        if evento.isEventRelatedtouser(request.user):
            myeventos.append(evento)
    contexto = {
        'eventos': eventos,
        'myeventos': myeventos
    }
    return render(request,
                  'eventos.html',
                  contexto)


def evento(request, id):
    contexto = {
        'evento': Evento.objects.get(id=id)
    }
    return render(request,
                  'evento.html',
                  contexto)
