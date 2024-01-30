
from django.db import models

class Vacancies(models):
    lang = models.CharField(max_length=16)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    url = models.URLField()
    salary = models.CharField(max_length=120)
    info = models.CharField(max_length=255)


'''
не знаю нужно ли вообще делать отдельную таблицу под иконки сайтов
с которых берутся вакансии 
'''
class Site_images(models):
    icon = models.ImageField()
    site_id = models.CharField(max_length=24)
