class CommandController():
    def __init__(self, constants, assistant, applicationController, internetResearchController, lightController, calendarController):
        self.constants = constants
        self.assistant = assistant
        self.applicationController = applicationController
        self.internetResearchController = internetResearchController
        self.lightController = lightController
        self.calendarController = calendarController
    
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
                    