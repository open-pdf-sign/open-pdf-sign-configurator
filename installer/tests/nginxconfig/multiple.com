server {
  server_name one.com;

  ssl_certificate      cert1.pem;
  ssl_certificate_key  cert1.key;
}

server {
  server_name two.com;
  ssl_certificate      cert2.pem;
  ssl_certificate_key  cert2.key;
}

# combined HTTP and HTTPS
server {
  server_name three.com four.com;
  listen 80;
  listen 5001 ssl;

  ssl_certificate      cert.pem;
  ssl_certificate_key  cert.key;
}
