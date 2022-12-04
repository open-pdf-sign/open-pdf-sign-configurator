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

####For releasing the python package run:
- python -m build
- twine upload -r testpypi dist/*
- twine upload -r pypi dist/*
