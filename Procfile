web: bash -lc "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn mcq.wsgi:application"
