FROM python:3.8

RUN mkdir djob_app

WORKDIR /djob_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /djob_project

CMD [ "python3 manage.py runserver" ]

