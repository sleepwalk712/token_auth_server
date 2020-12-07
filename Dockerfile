FROM python:3.8-alpine

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt
