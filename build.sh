docker compose down
docker build ./nginx/ -t nginx_custom --no-cache
docker compose up
