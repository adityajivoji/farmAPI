# farmAPI
```
docker build -t farmapi .
docker run -p 5000:5000 farmapi
```

```
docker run --name postgresDocker -p 5432:5432 -e POSTGRES_PASSWORD=adminaccess -d postgres

docker start postgreDocker

docker exec -it postgreDocker bash
psql -U postgres
CREATE DATABASE farmer_db;
docker run --name postgresDocker --network farmapi_network -p 5432:5432 -e POSTGRES_PASSWORD=adminaccess -d postgres
docker network connect farmapi_network postgreDocker
docker run --name farmapiapp --network farmapi_network -p 5000:5000 farmapi
```
https://stackoverflow.com/questions/52699899/depends-on-doesnt-wait-for-another-service-in-docker-compose-1-22-0
postgre


export SQLALCHEMY_DATABASE_URI=postgresql://postgres:adminaccess@localhost:5433/farmer_db
export SECRET_KEY=d58f5cf962eee2061
export JWT_SECRET_KEY=df8e5a7462e5c
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

sudo lsof -i -P -n | grep 5432

THINGS TO DO:
1. make the roles a list

docker build -t farmapi ./farmapi

docker tag farmapi:latest adityajivoji/farmapi:latest

docker tag nginx:latest adityajivoji/nginx:latest

docker push adityajivoji/farmapi:latest


docker push adityajivoji/nginx:latest

docker exec -it e5c65d879159 cat /var/log/uwsgi.log

docker stack rm farmapi_stack

docker stack deploy -c docker-compose.yml farmapi_stack


docker network create --driver overlay --attachable farmapi_overlay_network

<!-- Swarm initialized: current node (izw2ibsumarh4fwp0dv7hnom3) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-0pizdxsheqeotbjrndyt9kep79bg1244cbbiske7iw9top3leh-a72ppm48yyy5ry1d0hdafia4b 192.168.1.8:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions. -->

docker image prune -a

Swarm initialized: current node (vfocae98whtmnz3tfq4d23spp) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-4ql9ezrotdio7jce7zo6yun382l369tyygwkywhhlw6fyi8mzz-2l2imj0lil5mq2f5dhaawssb8 172.31.10.64:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.


docker build ./nginx/ -t nginx_custom --no-cache

docker build ./farmapi/ -t farmapi --no-cache


docker stack deploy -c docker-compose.yml farmapi_stack

docker service logs farmapi_stack_nginx_custom -fn0


docker exec -it 1ab70f194220 curl -X POST http://farmapi:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "superadmin", "password": "superpassword"}'
