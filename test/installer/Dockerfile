FROM ubuntu:latest
ARG domain=test.com
RUN apt update && apt install -y nginx openssl vim
RUN mkdir -p /var/www/$domain/html
RUN openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
    -subj "/C=AT/ST=open-pdf-sign/L=Vienna/O=Dis/CN=$domain" \
    -keyout $domain.key  -out $domain.cert
RUN cp $domain.* /etc/nginx
COPY default /etc/nginx/sites-available/
COPY test1.pdf /var/www/html
COPY test2.pdf /var/www/html
# nginx setup done

RUN apt update && apt install -y default-jre python3 python3-pip
#RUN pip install pyparsing==3.0.9 PyYAML requests==2.28.1
RUN pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple openpdfsign-configurator==1.0.8
COPY entrypoint.sh .
RUN chmod +x ./entrypoint.sh
EXPOSE 443
EXPOSE 80
CMD ./entrypoint.sh
