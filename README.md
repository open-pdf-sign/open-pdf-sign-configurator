# open-pdf-sign-configurator

## Requirements:
* ssh access to a server with sudo rights
* Webserver
	* NGinx
	* Apache (tbd)
* SSL certificate, for example from LetsEncrypt
* Unix based System
	* Ubuntu
	* Debian (tbd)


## How to Develop
First we create a mock ubuntu docker file
then we ssh into the ubuntuserver to install the open pdf sign installer
finally we open the website to show that it works

# development
- cd test/installer
- docker build -t nginx .
- docker exec -it installertest bash
- run: opsconfigurator
- press enter
- docker run --name installertest -d  -p 80:80 -p 443:443 nginx
- docker exec -d installertest java /etc/openpdfsign/openpdfsign.jar --config /etc/openpdfsign/config.yml   
visit: https://127.0.0.1/test1.pdf



