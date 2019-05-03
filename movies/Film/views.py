from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import *

# Create your views here.

def index(request):
    latest_film_list = Film.objects.order_by('annoUscita')[:30]
    template = loader.get_template('Film/index.html')
    context = {
        'latest_film_list' : latest_film_list
    }
    return HttpResponse(template.render(context, request))
    #output = '<br> '.join([f.titolo for f in latest_film_list])
    #return HttpResponse(output)

def detail(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    template = loader.get_template('Film/detail.html')
    context = {
        'film' : film
    }
    return HttpResponse(template.render(context, request))
    #output = "" +  film.titolo
    #return HttpResponse(output)

def attore(request, attore_id):
    attore = get_object_or_404(Attore, pk=attore_id)
    template = loader.get_template('Film/attore.html')
    context = {
        'attore' : attore
    }
    return HttpResponse(template.render(context, request))

def regista(request, regista_id):
    regista = get_object_or_404(Regista, pk=regista_id)
    template = loader.get_template('Film/regista.html')
    context = {
        'regista' : regista
    }
    return HttpResponse(template.render(context, request))