
from django.db import models

class Vacancies(models.Model):
    lang = models.CharField(max_length=16)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    url = models.URLField()
    salary = models.CharField(max_length=120)
    info = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.lang}, {self.title}, {self.company}, {self.url}, {self.salary}, {self.info}"
    