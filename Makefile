dev:
	poetry run python manage.py runserver

migrations:
	poetry run python manage.py makemigrations

show_sqlReq:
	poetry run python manage.py sqlmigrate $(m) $(v)

migrate:
	poetry run python manage.py migrate $(m) $(v)

lint:
	poetry run flake8 article hexlet_django_blog manage.py views.py