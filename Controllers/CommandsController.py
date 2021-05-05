import constants
from Controllers.ApplicationController import ApplicationController
from Controllers.CalendarController import CalendarController
from Controllers.InternetResearchController import InternetResearchController
from Controllers.LightController import LightController
from Controllers.WeatherController import WeatherController

class CommandController():
    def __init__(self, assistant, service):
        self.constants = constants
        self.assistant = assistant
        self.applicationController = ApplicationController(assistant, constants)
        self.internetResearchController = InternetResearchController(assistant, constants)
        self.lightController = LightController(constants)
        self.calendarController = CalendarController(constants, service, assistant)
        self.weatherController = WeatherController(assistant)
    
    def handleCommand(self, cmd):
        for x in self.constants.SKILLS:
            for i in self.constants.COMMANDS[x]:
                if i in cmd.lower():
                    self.switch(x, cmd)
                    break
                    

    def switch(self, x, cmd):
        if x == "fermer":
            self.assistant.speak("A bientôt monsieur.")
            self.assistant.actif = False
        elif x == "ouvrir":
            self.applicationController.applicationHandler(cmd)
        elif x == "chercher":
            self.internetResearchController.research(cmd)
        elif x == "heure":
            self.assistant.give_time()
        elif x == "lumière":
            self.lightController.process(cmd)
        elif x == "lire agenda":
            self.calendarController.handleCommand(cmd)
        elif x == "meteo":
            self.weatherController.handleCommand(cmd)                    