FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip3 install connexion[swagger-ui]

# RUN gunicorn --bind 0.0.0.0:$PORT wsgi

COPY . /usr/src/app

# ENTRYPOINT ["python3"]

CMD ["python3", "-m", "swagger_server", "gunicorn --bind 0.0.0.0:$PORT wsgi"]