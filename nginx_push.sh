docker build ./nginx/ -t nginx_custom

docker tag nginx_custom:latest adityajivoji/nginx_custom:latest

docker push adityajivoji/nginx_custom:latest