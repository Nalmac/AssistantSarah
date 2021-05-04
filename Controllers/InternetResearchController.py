import webbrowser
import wikipedia

class InternetResearchController():
    def __init__(self, assistant, constants):
        self.assistant = assistant
        self.online = assistant.internet_check()
        self.constants = constants

    def researchTypeDetect(self, entree):
        if entree is not None:
            if "youtube" in entree.lower():
                type = "youtube"
            elif "wikipédia" in entree.lower():
                type = "wikipédia"
            elif "duckduckgo" in entree.lower() or "cherche" in entree.lower() or "recherche" in entree.lower():
                type = "duckduckgo"
            return type
    
    def researchOnYoutube(self, entree):
        index = entree.lower().split().index("youtube")
        recherche = entree.lower().split()[index + 1:]
        if len(recherche) != 0:
            self.assistant.speak("Recherche sur Youtube")
            webbrowser.open("http://www.youtube.com/results?search_query=" + "+".join(recherche), new=2)
    
    def researchOnWikipedia(self, entree):
        wikipedia.set_lang("fr")
        try:
            recherche = entree.lower().replace("cherche sur wikipédia", "")
            if len(recherche) != 0:
                resultat = wikipedia.summary(recherche, sentences=1)
                self.assistant.speak("Recherche sur Wikipédia")
                self.assistant.speak(resultat)
        except:
            self.assistant.speak("Désolée, aucune page trouvée")
    
    def researchOnDDGo(self, entree):
        for i in self.constants.DDGO_SEARCH_TYPES:
            if i in entree.lower():
                index = entree.lower().split().index(i)
                recherche = entree.lower().split()[index + 1:]
                break
        if len(recherche) != 0:
            self.assistant.speak("Recherche sur Internet")
            webbrowser.open("https://duckduckgo.com/?q=" + "+".join(recherche), new=2)

    def research(self, entree):
        type = self.researchTypeDetect(entree)
        if type in ["duckduckgo", "youtube", "wikipédia"]:
            if type == "duckduckgo":
                self.researchOnDDGo(entree)
            elif type == "youtube":
                self.researchOnYoutube(entree)
            elif type == "wikipédia":
                self.researchOnWikipedia(entree)