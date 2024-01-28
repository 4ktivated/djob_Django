from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView



class ExampleView(TemplateView):
    template_name = 'some.html'

