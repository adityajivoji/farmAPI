FROM python:3.9-slim

RUN apt update

RUN apt install python3-pip -y
RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED=1
WORKDIR /farmapi
COPY . /farmapi
EXPOSE 5000
RUN pip install -r requirements.txt

CMD [ "uwsgi", "app.ini"]