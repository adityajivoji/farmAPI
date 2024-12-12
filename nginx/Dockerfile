FROM nginx:latest


# this should go to default.conf else you get 024/12/11 11:28:45 [error] 31#31: *2 open() "/usr/share/nginx/html/login" failed (2: No such file or directory), client: 172.19.0.1, server: localhost, request: "POST /login HTTP/1.1", host: "localhost"
# COPY default.conf /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/nginx.conf

