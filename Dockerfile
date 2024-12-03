FROM python:3.9-slim

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install --no-cache-dir flask flask-sqlalchemy


ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
EXPOSE 5000

CMD [ "python3", "farmapi.py"]