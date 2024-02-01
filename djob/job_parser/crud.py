from . import models
from . import handler

def create_vacs(lang: str):
    vacs = handler.VacHandler(lang).get_base()
    for el in vacs:
        models.Vacancies.objects.create(el)