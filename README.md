# farmAPI
```
docker build -t flask-app .
docker run -p 5000:5000 flask-app
```

```
docker run --name postgreDocker -p 5432:5432 -e POSTGRES_PASSWORD=adminaccess -d postgres

docker start postgreDocker

docker exec -it postgreDocker bash
CREATE DATABASE farmer_db;
```

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