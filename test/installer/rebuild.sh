#!/bin/sh
docker build -t nginx .
docker run -d  -p 80:80 -p 443:443 --privileged nginx
first get it runninng in docker
then make script that runs it
then make ssh
open -a "Google Chrome" https://127.0.0.1/x.pdf