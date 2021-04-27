FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip3 install connexion[swagger-ui]

COPY . /usr/src/app

# EXPOSE <port> keyword does not work with Heroku because Heroku decides what port
# our API runs on. To combat this, we bind their given port to $PORT and refer to it
CMD ["python3", "-m", "swagger_server", "gunicorn --bind 0.0.0.0:$PORT wsgi"]