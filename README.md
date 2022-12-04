# open-pdf-sign-configurator


## open-pdf-sign-configurator

This package can be used to install the open-pdf-sign server to sign all PDFs on your Nginx server
After you install this and activate it, all PDFs served by your Nginx server will automatically be signed by your 
SSL certificate for your domain being used by Nginx

For more details please go to  https://openpdfsign.org/ 
## Requirements
* Java 8 or higher
* python 3.9 or high
## Install
In order to install the configurator run
```bash
apt-get install default-jre python3 python3-pip
pip install openpdfsign-configurator
opsconfig
```


If you want to remove, remove relevant blocks in your Nginx config and run

```bash
rm /etc/systemd/system/openpdfsign.service
rm -rf /etc/openpdfsign
```


## Development
In order to develop, you can simply run the main.py file, just make sure to change the "stage" from "prod" to "test"

### Release
- python -m build
- twine upload -r testpypi dist/*
- twine upload -r pypi dist/*

#### Testing a release
In order to test you can run the following commands.

```bash 
cd test/installerrelease
docker build -t nginx .
docker run --name installertest -d  -p 80:80 -p 443:443 nginx
docker exec -it installertest bash
opsconfig
```
exit docker

```bash 
docker exec -d installertest java -jar /etc/openpdfsign/openpdfsign.jar --config /etc/openpdfsign/config.yml   
```
visit: https://127.0.0.1/test1.pdf


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
