from opsinstaller import nginxInstaller
from opsinstaller import utils

stage = "test"

if stage == "test":
    ymlConfigFilePath = "config.yml"
else:
    ymlConfigFilePath = "/etc/openpdfsign/config.yml"


def main():
    services = nginxInstaller.run(stage)
    # save all to yml file
    utils.saveConfigToYml(services, ymlConfigFilePath)
    utils.startServerAsService(ymlConfigFilePath)

# which java

# install via apt-get https://earthly.dev/blog/creating-and-hosting-your-own-deb-packages-and-apt-repo/+
