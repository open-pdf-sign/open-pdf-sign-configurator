# open-pdf-sign-configurator

open-pdf-sign-configurator is a tool that simplifies the process of setting up and configuring open-pdf-sign on an nginx server. It automates many of the steps involved in the installation and configuration process, making it quick and easy for users to get open-pdf-sign up and running on their web servers. This can help save time and reduce the potential for errors, allowing users to quickly and easily sign PDFs on their web server.

After you install and activate it, all PDFs served by your Nginx server will automatically be signed by your 
SSL certificate.

For more details please go to  https://openpdfsign.org/ 
## Requirements
* Java 8 or higher
* python 3.9 or higher
* Webserver (currently only Nginx supported)
* SSL certificate (tested with letsencrypt)

## Install
TLDR:

```bash
apt-get install default-jre python3 python3-pip
pip install openpdfsign-configurator
opsconfig
```

for detailed instructions please go to: [Instructions](https://github.com/open-pdf-sign/open-pdf-sign-configurator/blob/main/instructions.md)


If you want to remove, remove relevant blocks in your Nginx config and run

```bash
rm /etc/systemd/system/openpdfsign.service
rm -rf /etc/openpdfsign
```


## Development
* go to the "installer" folder
* create a virtual environment
* do pip install -r requirements.txt

In order to develop, you can simply run the main.py file, just make sure to change the "stage" from "prod" to "dev"

### Testing
This will create a docker container with:
- Nginx server running
- A certificate for test.com
- all dependencies installed

go to the file main.py in directory installer and change "prod" to "test"

```bash 
cd installer
python -m build
cp dist/*.whl ../test/installerdev
cd ../test/installerdev
vim Dockerfile #(change the version of the whl file if necessery)
docker build -t nginx .
docker run --name installertest -d  -p 80:80 -p 443:443 nginx
docker exec -it installertest bash
opsconfig
java -jar /etc/openpdfsign/openpdfsign.jar --config /etc/openpdfsign/config.yml   
```
visit: https://127.0.0.1/test1.pdf

### Release
- python -m build
- twine upload -r testpypi dist/*
- twine upload -r pypi dist/*

#### Testing a release
This will test the pypi test pip package.
In order to test you can run the following commands.

```bash 
cd test/installerrelease
docker build -t nginx .
docker run --name installertest -d  -p 80:80 -p 443:443 nginx
docker exec -it installertest bash
opsconfig
java -jar /etc/openpdfsign/openpdfsign.jar --config /etc/openpdfsign/config.yml   
```
visit: https://127.0.0.1/test1.pdf

## License

This project is licensed under the Apache 2.0-License. 
