import io

from opsconfig import menu
from opsconfig import nginxparser
from opsconfig import utils
from opsconfig.nginxConfigManipulator import NginxConfigManipulator


def run(stage="dev"):
    if stage == "dev":
        nginxConfigsDir = "tests/nginxconfig/"
    elif stage == "test":
        nginxConfigsDir = "/etc/nginx/sites-available/"
    else:
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
        if stage == "dev":
            nginxDump = nginxparser.dumps(installer.parsed)
            print(nginxDump)
        else:
            with io.open(installer.configFile, "w", encoding="utf-8") as config:
                nginxparser.dump(installer.parsed, config)
    return services
