FROM nginx:latest

RUN mkdir -p /etc/ssl/certs && mkdir -p /etc/ssl/private

COPY ./selfsigned.crt /etc/ssl/certs/selfsigned.crt
COPY ./selfsigned.key /etc/ssl/private/selfsigned.key

# Set permissions for the private key
RUN chmod 600 /etc/ssl/private/selfsigned.key

EXPOSE 443
EXPOSE 80

COPY nginx.conf /etc/nginx/nginx.conf



