import constants
import pyttsx3
import speech_recognition as sr
from urllib.request import urlopen
from random import randint
from datetime import datetime



class Assistant():
    
    def __init__(self):
        self.voix = pyttsx3.init()
        rate = self.voix.getProperty("rate")
        self.voix.setProperty("rate", rate-25)
        self.ear = sr.Recognizer()
        self.ear.energy_threshold = 4000
        self.misunderstood = "Désolé, je n'ai pas compris."
        self.actif = True
        self.constants = constants
    
    def speak(self, sortie):
        if sortie is not None:
            self.voix.say(sortie)
            self.voix.runAndWait()
    
    def internet_check(self):
        try:
            urlopen("https://www.google.com", timeout=1)
            return True
        except:
            return False
    
    def give_time(self):
        time = datetime.now()
        current_time = time.strftime("%H heures %M")
        self.speak("Il est " + current_time)
    
    def listenAndProcess(self):
        with sr.Microphone(device_index=3) as source:
            self.ear.adjust_for_ambient_noise(source)
            self.ear.pause_threshold = 0.7
            message = "Je vous écoute" if self.actif else ""
            print(message)
            audio = self.ear.listen(source)
            if self.internet_check():
                try:
                    vocal = self.ear.recognize_google(audio, language="fr-FR")
                    return vocal
                except sr.UnknownValueError:
                    self.speak(self.misunderstood)
            else:
                try:
                    vocal = self.ear.recognize_sphinx(audio, language="fr-fr")
                    return vocal
                except sr.UnknownValueError:
                    self.speak(self.misunderstood)
    
    def listenForCall(self):
        with sr.Microphone(device_index=3) as source:
            self.ear.adjust_for_ambient_noise(source)
            self.ear.pause_threshold = 0.7
            audio = self.ear.listen(source)
            vocal = "dodo"
            try:
                if self.internet_check():
                    vocal = self.ear.recognize_google(audio, language="fr-FR")
                else:
                    vocal = self.ear.recognize_sphinx(audio, language="fr-fr")
                print(vocal)
            except:
                pass
            for i in self.constants.CALL_WORDS:
                if i in vocal.lower():
                    self.speak(self.constants.LINES[randint(0, 4)])
                    self.actif = True


