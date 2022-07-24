FROM ubuntu:latest
ARG domain=test.com
RUN apt update && apt install -y nginx openssl
RUN mkdir -p /var/www/$domain/html
RUN openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
    -subj "/C=AT/ST=open-pdf-sign/L=Vienna/O=Dis/CN=$domain" \
    -keyout $domain.key  -out $domain.cert
RUN cp $domain.* /etc/nginx
COPY default /etc/nginx/sites-available/
EXPOSE 443
EXPOSE 80
CMD /usr/sbin/nginx -g "daemon off;"
