docker stack rm farmapi_stack


sleep 5

docker stack deploy -c docker-compose.yml farmapi_stack
