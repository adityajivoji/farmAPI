FROM python:3.9-slim

RUN apt update
RUN apt install python3-pip -y
RUN apt-get install libpcre3 libpcre3-dev -y
RUN pip install --upgrade pip
ENV PYTHONUNBUFFERED=1
WORKDIR /farmapi
COPY . /farmapi
# RUN pip install uwsgi -I
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["gunicorn","--workers=5","-b","0.0.0.0:5000","farmapi:create_app()","--timeout","0"]