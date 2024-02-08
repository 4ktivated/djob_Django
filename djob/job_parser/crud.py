from django.shortcuts import render
from . import models
from . import handler


def create_vacs(lang: str):
    vacs = handler.VacHandler(lang).fill_data()
    for el in vacs:
        models.Vacancies.objects.create(lang=el.get('lang'),
                                title=el.get('title'),
                                company=el.get('company'),
                                url=el.get('url'), 
                                salary=el.get('salary'), 
                                info=el.get('info'))
        

def get_vacs_by_lang(lang: str):
    return models.Vacancies.objects.filter(lang=lang)
    

def clear_base():
    models.Vacancies.objects.all().delete()
