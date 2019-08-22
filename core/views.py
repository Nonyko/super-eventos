from django.shortcuts import render

# Create your views here.
from core.models import Evento
from .forms import EventoForm

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

def criarevento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        print(form)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.owner = request.user
            print(evento)
            #evento.save()
    else:
        form = EventoForm()

    contexto = {
    'form' : form
    }
    return render(request,
                  'formevento.html',
                  contexto)
