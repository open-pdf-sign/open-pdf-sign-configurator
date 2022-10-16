FROM ubuntu:latest
ARG domain=test.com
RUN apt update && apt install -y nginx openssl vim
RUN mkdir -p /var/www/$domain/html
RUN openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
    -subj "/C=AT/ST=open-pdf-sign/L=Vienna/O=Dis/CN=$domain" \
    -keyout $domain.key  -out $domain.cert
RUN cp $domain.* /etc/nginx

# nginx setup done
RUN apt update && apt install -y fcgiwrap default-jre
COPY default /etc/nginx/sites-available/
COPY openpdfsign.jar .
COPY entrypoint.sh .
COPY test1.pdf /var/www/html
COPY test2.pdf /var/www/html
RUN chmod +x ./entrypoint.sh
EXPOSE 443
EXPOSE 80
CMD ./entrypoint.sh
