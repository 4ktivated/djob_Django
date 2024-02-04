from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from . import crud


def fill_base(request, lang):
    crud.create_vacs(lang)
    return HttpResponse('all works good')

def get_vbl(request, lang):
    return HttpResponse(crud.get_vacs_by_lang(lang))


class ExampleView(TemplateView):
    template_name = 'some.html'

