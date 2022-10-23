import os

import nginxparser
import menu


class Installer:
    exe = "nginx"
    configFile = "both.com"
    parsed = None

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

        # get location of keys
        # ssl_certificate
        # ssl_certificate_key

        keys = []
        # check each server block
        for server in self.parsed:
            # check all elements in server block
            for element in server:
                if len(element) > 0 and element[0] != "server":
                    key = {}
                    for el in element:
                        if el[0] == "server_name":
                            key["server_name"] = el[1]
                        if el[0] == "ssl_certificate":
                            key["ssl_certificate"] = el[1]
                        if el[0] == "ssl_certificate_key":
                            key["ssl_certificate_key"] = el[1]

                        if len(key.keys()) == 3:
                            keys.append(key)
                if element == "#":
                    if "managed by open-pdf-sign" in server[1]:
                        print(keys[-1]["server_name"], "already configured")
        return keys

    def insertBlocks(self, selection):
        directive = [['\n    ', 'location', ' ', '~', ' ', '\\.(pdf)$', ' '],[
                     ['\n    ', 'proxy_set_header', ' ', 'X-Forwarded-For', ' ', '$proxy_add_x_forwarded_for', ' '],
                     ['\n    ', 'proxy_set_header', ' ', 'X-Forwarded-Proto', ' ', '$scheme'],
                     ['\n    ', 'proxy_set_header', ' ', 'X-Real-IP', ' ', '$remote_addr'],
                     ['\n    ', 'proxy_set_header', ' ', 'Host', ' ', '$http_host'],
                     ['\n    ', 'proxy_set_header', ' ', 'X-Open-Pdf-Sign-Nginx-Version', ' ', '$1.0.0'],
                     ['\n    ', 'proxy_set_header', ' ', 'X-Open-Pdf-Sign-File', ' ', '$document_root$uri'],
                     ['\n    ', 'proxy_pass', ' ', 'http://127.0.0.1:8090/v1/sign'],
                     ['\n    ', 'proxy_redirect', ' ', 'off'],
                     ['\n    ', '}', ' ', '#', ' ', 'managed by open-pdf-sign-configurator']]]
        #	} # managed by open-pdf-sign-configurator
        self.parsed[6][1].insert(3, directive)


installer = Installer()
info = installer.getNginxInfo()
selection = menu.installMenu(info)
installer.insertBlocks(selection)
dump = nginxparser.dumps(installer.parsed)
print(dump)
print("test")
