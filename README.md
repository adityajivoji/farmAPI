# farmAPI
```
docker build -t farmapi .
docker run -p 5000:5000 farmapi
```

```
docker run --name postgreDocker -p 5432:5432 -e POSTGRES_PASSWORD=adminaccess -d postgres

docker start postgreDocker

docker exec -it postgreDocker bash
CREATE DATABASE farmer_db;
docker run --name postgreDocker --network farmapi_network -p 5432:5432 -e POSTGRES_PASSWORD=adminaccess -d postgres
docker network connect farmapi_network postgreDocker
docker run --name farmapiapp --network farmapi_network -p 5000:5000 farmapi
```
https://stackoverflow.com/questions/52699899/depends-on-doesnt-wait-for-another-service-in-docker-compose-1-22-0
postgre

# Authentication

## Users


superUser
- can add admin and make any changes to the database

admin
- can add user and access any api

user
- can access only GET Methods

we have to separate the functionality of router, service, repository

find . -type d -name "__pycache__" -exec rm -rf {} +

THINGS TO DO:
1. make the roles a list