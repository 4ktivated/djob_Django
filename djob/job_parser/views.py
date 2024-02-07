from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import TemplateView
from . import crud


def fill_base(request, lang):
    crud.create_vacs(lang)
    return HttpResponse('all works good')

def get_vbl(request, lang):
    return render(request, 'job_parser/some.html',{"vac_list": crud.get_vacs_by_lang(lang=lang)})

def not_found(request, exception):
    return HttpResponseNotFound('<h1>Такой страницы нет</h1>')

class ExampleView(TemplateView):
    template_name = 'some.html'

