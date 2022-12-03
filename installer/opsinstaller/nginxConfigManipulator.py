import os

from opsinstaller import nginxparser


class NginxConfigManipulator:
    exe = "nginx"
    configFile = ""
    parsed = None

    def __init__(self, configFile):
        self.configFile = configFile

    def checkExe(self, exe):
        path, _ = os.path.split(exe)
        if path and os.path.isfile(path) and os.access(path, os.X_OK):
            pass
        else:
            return False
        for path in os.environ["PATH"].split(os.pathsep):
            newExe = os.path.join(path, exe)
            if newExe and os.path.isfile(newExe) and os.access(newExe, os.X_OK):
                return True

    def getNginxInfo(self):
        # check if nginx exists
        self.checkExe("nginx")
        # check if config is ok
        # nginx -t
        with open(self.configFile) as filee:
            self.parsed = nginxparser.load(filee)

        keys = []
        # check each server block
        counter = 0
        for server in self.parsed:
            # check all elements in server block
            for element in server:
                if len(element) > 0 and element[0] != "server":
                    key = {}
                    for el in element:
                        key["index"] = counter
                        if el[0] == "server_name":
                            key["host"] = [el[e] for e in range(1,len(el))]
                        if el[0] == "ssl_certificate":
                            key["certificate"] = el[1]
                        if el[0] == "ssl_certificate_key":
                            key["key"] = el[1]

                        if len(key.keys()) == 4:
                            keys.append(key)
                            break
                if element == "#":
                    if "managed by open-pdf-sign" in server[1]:
                        print(keys[-1]["server_name"], "already configured")
            counter += 1
        return keys

    def insertBlocks(self, selection):
        port = '8090'
        position = 0
        directive = [['\n    ', 'location', ' ', '~', ' ', '\\.(pdf)$', ' '], [
            ['\n    ', 'proxy_set_header', ' ', 'X-Forwarded-For', ' ', '$proxy_add_x_forwarded_for', ' '],
            ['\n    ', 'proxy_set_header', ' ', 'X-Forwarded-Proto', ' ', '$scheme'],
            ['\n    ', 'proxy_set_header', ' ', 'X-Real-IP', ' ', '$remote_addr'],
            ['\n    ', 'proxy_set_header', ' ', 'Host', ' ', '$http_host'],
            ['\n    ', 'proxy_set_header', ' ', 'X-Open-Pdf-Sign-Nginx-Version', ' ', '1.0.0'],
            ['\n    ', 'proxy_set_header', ' ', 'X-Open-Pdf-Sign-File', ' ', '$document_root$uri'],
            ['\n    ', 'proxy_pass', ' ', 'http://127.0.0.1:' + port + '/v1/sign$1'],
            ['\n    ', 'proxy_redirect', ' ', 'off'],
        ]]
        comment = [' ', '#', ' managed by open-pdf-sign-configurator']
        for serverBlock in selection:
            self.parsed[serverBlock][1].insert(position, directive)
            self.parsed[serverBlock][1].insert(position + 1, comment)
