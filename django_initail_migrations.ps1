docker-compose exec django python manage.py makemigrations
exec django python manage.py migrate
docker-compose exec django python manage.py createsuperuser