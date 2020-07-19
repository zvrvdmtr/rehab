Reabilitation for people with injuries.

## You can run this application using docker:
1. Run container with DB  
    ```docker run --rm --name pg-docker -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres:12```
2. Run application with Django server  
    ```docker-compose up -d```
3. Create django superuser  
    1. ```docker exec -it 9452be272545 python manage.py createsuperuser```
    2. Follow instructions

After created superuser you will be able to create db models using django admin.

## Endpoints

### Django admin:
1. ```127.0.0.1:8000/admin```

### API:  
1. ```http://127.0.0.1:8000/api/v1/events``` (GET, POST)
2. ```http://127.0.0.1:8000/api/v1/event/%event_id%``` (GET, PUT, DELETE)
3. ```http://127.0.0.1:8000/api/v1/practices``` (NOT IMPLEMENTED)
4. ```http://127.0.0.1:8000/api/v1/practice/%practice_id%``` (NOT IMPLEMENTED)
    