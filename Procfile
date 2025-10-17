web: gunicorn bookstore.wsgi --workers 3 --worker-class sync --bind 0.0.0.0:$PORT --log-file -
release: python manage.py migrate