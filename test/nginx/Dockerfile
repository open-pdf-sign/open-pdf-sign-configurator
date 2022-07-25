FROM ubuntu:latest
ARG domain=test.com
RUN apt update && apt install -y nginx openssl vim
RUN mkdir -p /var/www/$domain/html
RUN openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
    -subj "/C=AT/ST=open-pdf-sign/L=Vienna/O=Dis/CN=$domain" \
    -keyout $domain.key  -out $domain.cert
RUN cp $domain.* /etc/nginx
RUN apt update && apt install -y fcgiwrap
COPY default /etc/nginx/sites-available/
COPY x.pdf /var/www/
COPY entrypoint.sh .
RUN chmod +x /var/www/x.pdf
RUN chmod +x ./entrypoint.sh
EXPOSE 443
EXPOSE 80
CMD ./entrypoint.sh
