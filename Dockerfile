FROM python:3.9-alpine

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt
