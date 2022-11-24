import os
import subprocess
from yaml import dump


def saveConfigToYml(services, configFile):
    config = {}
    config["port"] = 8081
    config["host"] = "127.0.0.1"
    for service in services:
        service.pop("index", None)
        service["host"] = " ".join(service["host"])
    config["certificates"] = services
    with open(configFile, 'w') as ymlConfig:
        dump(config, ymlConfig)
    pass

def createInstallDirs( path):
    isdir = os.path.isdir(path)
    if not isdir:
        os.mkdir(path)

def getNginxConfigs( path):
    paths = os.listdir(path)
    return paths
def startServerAsService(configFile, installpath):
    subprocess.check_output("cp openpdfsign.service /etc/systemd/system/", shell=True)
    subprocess.check_output()
    # write the service file
    # (re)start service
    pass
