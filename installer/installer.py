import nginxparser
import menu
import utils
from nginxInstaller import NginxInstaller

configFile = "tests/nginxconfig/multiple.com"
ymlConfigFilePath = "config.yml"

installer = NginxInstaller(configFile)
info = installer.getNginxInfo()
print(info)
selection = menu.installMenu(info)
installer.insertBlocks(selection)
nginxDump = nginxparser.dumps(installer.parsed)
print(nginxDump)
# save all to yml file
utils.saveConfigToYml(selection, ymlConfigFilePath )
utils.startServerAsService(ymlConfigFilePath)

# which java

# https://github.com/rtr-nettest/rmbt-server/blob/master/rmbt.service
# install via apt-get https://earthly.dev/blog/creating-and-hosting-your-own-deb-packages-and-apt-repo/+
