from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from . import crud, models


def refil_base(request, lang):
    crud.create_vacs(lang)
    return models.Vacancies.objects.all()


class ExampleView(TemplateView):
    template_name = 'some.html'

