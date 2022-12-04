# Installation Instructions for open-pdf-sign
Following these instructions will make all PDFs served by your webserver signed by your SSL certificate

## Requirements
- comfort with the command line
- a Nginx webserver that is online and running debian or Ubuntu
- a LetsEncrypt or other SSL certificate installed with Nginx
- SSH access to your server with sudo rights

## Installation

### 1. SSH into your server

SSH into the server running your HTTP website as a user with sudo privileges.
### 2. Install Dependencies
```bash
apt-get install default-jre python3 python3-pip
```
### 3. Install openpdfsign-configurator
```bash
pip install openpdfsign-configurator
```
### 4. Run the Configurator
```bash
opsconfig
```
You can select the domain names where open-pdf-sign will be installed
### 5. Confirm that its working

Go to the URL where you are currently serving a PDF
Download it and check your signature i.e. here: https://ec.europa.eu/cefdigital/DSS/webapp-demo/validation
