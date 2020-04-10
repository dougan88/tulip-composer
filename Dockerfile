FROM python:alpine3.8
COPY . /app
WORKDIR /app

CMD python3 app.py
