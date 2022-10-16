#!/bin/sh
service fcgiwrap start
java -jar openpdfsign.jar -i input.pdf -o output.pdf \
  -c /etc/nginx/test.com.cert \
  -k /etc/nginx/test.com.key \
  --port 8090 --host 127.0.0.1 &
echo "all started"
/usr/sbin/nginx -g "daemon off;"
