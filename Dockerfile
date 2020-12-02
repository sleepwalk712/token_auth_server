FROM python:3.7-alpine3.11

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt
