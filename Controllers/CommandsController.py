import constants
import random
from Controllers.ApplicationController import ApplicationController
from Controllers.CalendarController import CalendarController
from Controllers.InternetResearchController import InternetResearchController
from Controllers.LightController import LightController
from Controllers.WeatherController import WeatherController
from Language.LanguageProcessor import LanguageProcessor
import json

class CommandController():
    def __init__(self, assistant, service):
        self.constants = constants
        self.assistant = assistant
        self.applicationController = ApplicationController(assistant, constants)
        self.internetResearchController = InternetResearchController(assistant, constants)
        self.lightController = LightController(constants)
        self.calendarController = CalendarController(constants, service, assistant)
        self.weatherController = WeatherController(assistant)
        self.languageProcessor = LanguageProcessor()
    
    def handleCommand(self, cmd):
        x = self.languageProcessor.processText(cmd)
        self.switch(x, cmd)
                    

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
        elif x == "lumiere":
            self.lightController.process(cmd)
        elif x == "lire agenda":
            self.calendarController.handleCommand(cmd)
        elif x == "meteo":
            self.weatherController.handleCommand(cmd)
        else:
            self.speakLine(x)

    def speakLine(self, tag):
        intents = json.load(open("./Language/intents.json"))["intents"]
        lines = []
        for intent in intents:
            if intent["tag"] == tag:
                lines = intent["responses"]
                break
        print(tag)
        self.assistant.speak(lines[random.randint(0, len(lines) - 1)])
