import nginxparser
import menu
import utils
from nginxInstaller import NginxInstaller

#ymlConfigFilePath = "/etc/openpdfsign/config.yml"
ymlConfigFilePath = "config.yml"

# configFile = "tests/nginxconfig/multiple.com"
# nginxConfigs = utils.getNginxConfigs("/etc/nginx/sites-available")
nginxConfigsDir = "tests/nginxconfig/"
nginxConfigs = utils.getNginxConfigs(nginxConfigsDir)
installers = []
for nginxConfig in nginxConfigs:
    configFile = nginxConfig
    installer = NginxInstaller(nginxConfigsDir + configFile)
    installers.append(installer)
selection, infos = menu.installMenu(installers)

services = []
for i in range(len(infos)):
    installer = installers[i]
    service = [infos[i][s] for s in selection[i]]
    services.extend(service)
    installer.insertBlocks([s["index"] for s in service])
    nginxDump = nginxparser.dumps(installer.parsed)
    print(nginxDump)

# save all to yml file
utils.saveConfigToYml(services, ymlConfigFilePath)
utils.startServerAsService(ymlConfigFilePath)

# which java

# install via apt-get https://earthly.dev/blog/creating-and-hosting-your-own-deb-packages-and-apt-repo/+
