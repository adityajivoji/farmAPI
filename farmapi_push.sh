docker build ./farmapi/ -t farmapi

docker tag farmapi:latest adityajivoji/farmapi:latest

docker push adityajivoji/farmapi:latest