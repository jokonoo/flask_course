FROM python:3.11-slim
ENV PYTHONBUFFERED True
ENV PYTHONPATH /flask_app/src
WORKDIR /flask_app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt