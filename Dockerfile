FROM python:3.10

WORKDIR /app
COPY . /app
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
