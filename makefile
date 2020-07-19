docker-run-app:
	python3 ./utils/wait_postgres.py
	python3 manage.py migrate
	python3 manage.py runserver 0.0.0.0:8000