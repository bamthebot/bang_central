FROM python:3.7.3

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/bam/bangcentral/
WORKDIR /home/bam/bangcentral

COPY . /home/bam/bangcentral

RUN python3 -m venv venv && . venv/bin/activate
RUN pip install -r requirements.txt
RUN python3 manage.py makemigrations && python3 manage.py migrate

CMD gunicorn --bind 0.0.0.0:8000 bang_central.wsgi 
