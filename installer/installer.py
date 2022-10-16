import os

import nginxparser

exe = "nginx"
configFile = "both.com"

def checkExe(exe):
    path, _ = os.path.split(exe)
    if path and os.path.isfile(path) and os.access(path, os.X_OK):
        pass
    else:
        return False
    for path in os.environ["PATH"].split(os.pathsep):
        newExe = os.path.join(path, exe)
        if newExe and os.path.isfile(newExe) and os.access(newExe, os.X_OK):
            return True

# check if nginx exists
checkExe("nginx")
# check if config is ok
# nginx -t
with open(configFile) as filee:
    parsed = nginxparser.load(filee)

print(parsed)
