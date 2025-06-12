web: gunicorn bookstore.wsgi:application --bind 0.0.0.0:$PORT

python-3.11.9

build:
  docker:
    web: Dockerfile
run:
  web: gunicorn bookstore.wsgi:application --bind 0.0.0.0:$PORT

SECRET_KEY=sua-secret-key-muito-segura-aqui
DATABASE_URL=postgres://usuario:senha@host:porta/database
DEBUG=False
ALLOWED_HOSTS=sua-app.herokuapp.com,www.sua-app.herokuapp.com
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=sua-senha-de-app
DEFAULT_FROM_EMAIL=noreply@sua-app.herokuapp.com
REDIS_URL=redis://localhost:6379/1
CORS_ALLOWED_ORIGINS=https://sua-app.herokuapp.com