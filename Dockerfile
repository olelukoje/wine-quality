FROM python:3.7.1-stretch

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt

EXPOSE 80

CMD [ "gunicorn", "-b", "0.0.0.0:80", "predicts_api:app" ]
