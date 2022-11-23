import nginxparser
import menu
import utils
from nginxInstaller import NginxInstaller

ymlConfigFilePath = "/etc/openpdfsign/config.yml"

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

for i in range(len(infos)):
    installer = installers[i]
    installer.insertBlocks([infos[i][s]["index"] for s in selection[i]])
    nginxDump = nginxparser.dumps(installer.parsed)
    print(nginxDump)

# save all to yml file
utils.saveConfigToYml(selection, ymlConfigFilePath)
utils.startServerAsService(ymlConfigFilePath)

# which java

# https://github.com/rtr-nettest/rmbt-server/blob/master/rmbt.service
# install via apt-get https://earthly.dev/blog/creating-and-hosting-your-own-deb-packages-and-apt-repo/+
