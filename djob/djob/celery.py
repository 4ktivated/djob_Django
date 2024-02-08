import os
from celery import Celery
from job_parser.crud import clear_base, create_vacs

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djob.settings")
celery = Celery("djob")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()

@celery.task
def up_base():
    implment_lang = ['php', 'python', 'go', 'java']
    for lang in implment_lang:
        create_vacs(lang)


@celery.task
def down_base():
    clear_base()