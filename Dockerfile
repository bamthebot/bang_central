FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/bam/bangcentral/
WORKDIR /home/bam/bangcentral

COPY . /home/bam/bangcentral

RUN python -m venv venv && . venv/bin/activate
RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:8000 bang_central.wsgi 
