from pythontools.core import tools
import os

class Config(object):

    def __init__(self, path="", default_config={}):
        self.path = path
        if "%APPDATA%" in self.path:
            self.path = self.path.replace("%APPDATA%", str(os.getenv("APPDATA")))
        if not tools.existDirectory(self.path):
            try:
                tools.createDirectory(self.path)
            except:
                pass
        if not tools.existFile(self.path + "config.json"):
            tools.createFile(self.path + "config.json")
            tools.saveJson(self.path + "config.json", default_config)
        self.config = tools.loadJson(self.path + "config.json")

    def getConfig(self):
        return self.config

    def saveConfig(self):
        tools.saveJson(self.path + "config.json", self.config)
