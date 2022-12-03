from opsinstaller import nginxInstaller
from opsinstaller import utils

stage = "prod"
installpath = "/etc/openpdfsign/"
ymlConfigFilePath = installpath + "config.yml"
if stage == "test":
    ymlConfigFilePath = "config.yml"
    installpath = "./"


def main():
    services = nginxInstaller.run(stage)
    # save all to yml file
    utils.createInstallDirs(installpath)
    utils.saveConfigToYml(services, ymlConfigFilePath)
    utils.startServerAsService(ymlConfigFilePath, installpath, stage)


if stage == "test":
    main()
# which java

# install via apt-get https://earthly.dev/blog/creating-and-hosting-your-own-deb-packages-and-apt-repo/
# https://medium.com/@benmorel/creating-a-linux-service-with-systemd-611b5c8b91d6
# https://realpython.com/pypi-publish-python-package/#prepare-your-package-for-publication
