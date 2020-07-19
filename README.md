Reabilitation for people with injuries.

## You can run this application using docker:
1. Run application with Django server
    ```docker-compose up -d```
2. Create django superuser  
    1. ```docker exec -it rehab_app python manage.py createsuperuser```
    2. Follow instructions

## You can run this application using db inside docker
1. Run container with DB  
    ```docker run --rm --name pg-docker -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres:12```
2. Pull this repo
3. Run migrations  
    ```python manage.py migrate```
4. Create django superuser  
    1. ```python manage.py createsuperuser```
    2. Follow instructions
5. Run app  
    ```python manage.py runserver```

After created superuser you will be able to create db models using django admin.

## Endpoints

### Django admin:
1. ```127.0.0.1:8000/admin```

### API:  
1. ```http://127.0.0.1:8000/api/v1/events``` (GET, POST)
2. ```http://127.0.0.1:8000/api/v1/event/%event_id%``` (GET, PUT, DELETE)
3. ```http://127.0.0.1:8000/api/v1/practices``` (NOT IMPLEMENTED)
4. ```http://127.0.0.1:8000/api/v1/practice/%practice_id%``` (NOT IMPLEMENTED)
    