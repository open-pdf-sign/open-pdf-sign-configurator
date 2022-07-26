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
}
