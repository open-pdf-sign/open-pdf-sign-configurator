import io

from opsconfig import menu
from opsconfig import nginxparser
from opsconfig import utils
from opsconfig.nginxConfigManipulator import NginxConfigManipulator


def run(stage="test"):
    if stage == "test":
        nginxConfigsDir = "tests/nginxconfig/"
        ymlConfigFilePath = "config.yml"
    else:
        ymlConfigFilePath = "/etc/openpdfsign/config.yml"
        nginxConfigsDir = "/etc/nginx/sites-available/"

    nginxConfigs = utils.getNginxConfigs(nginxConfigsDir)
    installers = []
    for nginxConfig in nginxConfigs:
        configFile = nginxConfig
        installer = NginxConfigManipulator(nginxConfigsDir + configFile)
        installers.append(installer)
    selection, infos = menu.installMenu(installers)

    services = []
    for i in range(len(infos)):
        installer = installers[i]
        service = [infos[i][s] for s in selection[i]]
        services.extend(service)
        installer.insertBlocks([s["index"] for s in service])
        if stage == "test":
            nginxDump = nginxparser.dumps(installer.parsed)
            print(nginxDump)
        else:
            with io.open(installer.configFile, "w", encoding="utf-8") as config:
                nginxparser.dump(installer.parsed, config)
    return services
