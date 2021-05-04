import subprocess as sp

class ApplicationController():
    def __init__(self, assistant, constants):
        self.assistant = assistant
        self.constants = constants
    
    def applicationDetect(self, entree):
        if entree is None:
            return
        app = "Unknown"
        for i in self.constants.KNOWN_APPS:
            for x in self.constants.APPS[i]:
                if x in entree.lower():
                    app = i
        return app

    def applicationOpen(self, app):
        self.assistant.speak("Ouverture de " + self.constants.NAMES[app])
        sp.Popen(self.constants.PATHS[app])
    
    def applicationHandler(self, entree):
        app = self.applicationDetect(entree)
        if app in self.constants.KNOWN_APPS:
            self.applicationOpen(app)
        else:
            self.assistant.speak("Désolée, je ne connaîs pas cette application")