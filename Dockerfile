FROM python:3.9-slim

RUN apt update
RUN apt install python3-pip -y
RUN pip install --upgrade pip




ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN flask db init
RUN flask db migrate
RUN flask db upgrade
EXPOSE 5000

CMD [ "python3", "run.py"]