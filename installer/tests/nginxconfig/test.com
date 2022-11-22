server {
  server_name ssl.both.com;
}



# combined HTTP and HTTPS
server {
  server_name ssl.both.com;
  listen 80;
  listen 5001 ssl;

  ssl_certificate      cert.pem;
  ssl_certificate_key  cert.key;

}

# HTTPS, duplicate by means of wildcard
server {
  server_name *..com;
  listen 5001 ssl;

  ssl_certificate      cert.pem;
  ssl_certificate_key  cert.key;
    location ~ \.(pdf)$ {
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto $scheme;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header Host $http_host;
		proxy_set_header X-Open-Pdf-Sign-Nginx-Version 1.0.0;
		proxy_set_header X-Open-Pdf-Sign-File: $document_root$uri;
		proxy_pass http://127.0.0.1:8090/v1/sign;
		proxy_redirect off;
	} # managed by open-pdf-sign-configurator
}
