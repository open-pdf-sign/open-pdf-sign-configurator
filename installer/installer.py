import nginxparser
import menu
import utils
from nginxInstaller import NginxInstaller

configFile = "multiple.com"
ymlConfigFilePath = "config.yml"

installer = NginxInstaller(configFile)
info = installer.getNginxInfo()
print(info)
selection = menu.installMenu(info)
installer.insertBlocks(selection)
dump = nginxparser.dumps(installer.parsed)
print(dump)
# save all to yml file
utils.saveConfigToYml(selection, ymlConfigFilePath )
utils.startServerAsService(ymlConfigFilePath)

# which java

# https://github.com/rtr-nettest/rmbt-server/blob/master/rmbt.service
# install via apt-get https://earthly.dev/blog/creating-and-hosting-your-own-deb-packages-and-apt-repo/+
