import os
import subprocess
import requests
from yaml import dump


jarUrl = "https://github.com/open-pdf-sign/open-pdf-sign/releases/download/v0.0.2-rc.1/open-pdf-sign.jar"
serviceContent = "[Unit]\n" \
                 "Description=Open-Pdf-Sign-Server\n" \
                 "\n" \
                 "[Install]\n" \
                 "WantedBy=multi-user.target\n" \
                 "\n" \
                 "[Service]\n" \
                 "Restart=always\n" \
                 "User=root\n" \
                 "StandardOutput=null\n" \
                 "StandardError=journal\n" \
                 "ExecStart=/usr/bin/java -jar openpdfsignserver.jar --config "


def saveConfigToYml(services, configFile):
    config = {}
    config["port"] = 8090
    config["host"] = "127.0.0.1"
    for service in services:
        service.pop("index", None)
        service["host"] = " ".join(service["host"])
    config["certificates"] = services
    with open(configFile, 'w') as ymlConfig:
        dump(config, ymlConfig)
    pass


def createInstallDirs(path):
    isdir = os.path.isdir(path)
    if not isdir:
        os.mkdir(path)


def getNginxConfigs(path):
    paths = os.listdir(path)
    return paths


def startServerAsService(configFile, installpath):
    with open("/etc/systemd/system/openpdfsign.service", "w") as serviceFile:
        serviceFile.write(serviceContent + configFile)
    r = requests.get(jarUrl, allow_redirects=True)
    with open(installpath+"openpdfsign.jar") as jarFile:
        jarFile.write(r.content)

    subprocess.check_output("service nginx reload")
    subprocess.check_output("systemctl enable openpdfsign")
    subprocess.check_output("systemctl start openpdfsign")
    # write the service file
    # (re)start service