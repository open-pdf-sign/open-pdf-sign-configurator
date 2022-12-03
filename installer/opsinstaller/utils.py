import os
import sys
import subprocess
import requests
from yaml import dump

jarUrl = "https://github.com/open-pdf-sign/open-pdf-sign/releases/latest/download/open-pdf-sign.jar"
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


def startServerAsService(configFile, installpath, stage="prod"):
    if stage == "prod":
        with open("/etc/systemd/system/openpdfsign.service", "w") as serviceFile:
            serviceFile.write(serviceContent + configFile)
    with open(installpath + "openpdfsign.jar", "wb") as jarFile:
        print("Downloading jar file")
        response = requests.get(jarUrl, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None:  # no content length header
            jarFile.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                jarFile.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush()
    if stage == "prod":
        subprocess.run("service nginx reload;echo;", shell=True)
        subprocess.run("chmod +x /etc/openpdfsign/openpdfsign.jar", shell=True)
    # write the service file
    # subprocess.check_output("systemctl enable openpdfsign")
    # subprocess.check_output("systemctl start openpdfsign")
    # (re)start service
