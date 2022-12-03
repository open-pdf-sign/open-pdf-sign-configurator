from opsconfig import nginxInstaller
from opsconfig import utils

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

# install via apt-get https://earthly.dev/blog/creating-and-hosting-your-own-deb-packages-and-apt-repo/
