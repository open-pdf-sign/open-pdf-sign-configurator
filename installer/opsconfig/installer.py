from opsconfig import nginxInstaller
from opsconfig import utils

# can be: "test", "prod" or "dev"
stage = "test"
installpath = "/etc/openpdfsign/"
ymlConfigFilePath = installpath + "config.yml"
if stage == "dev":
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
