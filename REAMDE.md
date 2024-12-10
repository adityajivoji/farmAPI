docker network create --driver overlay --attachable farmapi_overlay_network

<!-- Swarm initialized: current node (izw2ibsumarh4fwp0dv7hnom3) is now a manager.

To add a worker to this swarm, run the following command:

    docker swarm join --token SWMTKN-1-0pizdxsheqeotbjrndyt9kep79bg1244cbbiske7iw9top3leh-a72ppm48yyy5ry1d0hdafia4b 192.168.1.8:2377

To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions. -->

docker stack rm farmapi_stack
docker image prune -a


docker build ./nginx/ -t nginx_custom --no-cache

docker build ./farmapi/ -t farmapi --no-cache


docker stack deploy -c docker-compose.yml farmapi_stack

docker service logs farmapi_stack_nginx_custom -fn0


docker exec -it 1ab70f194220 curl -X POST http://farmapi:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "superadmin", "password": "superpassword"}'
