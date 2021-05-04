#-----------------------------------------------------------------------Config de l'assistant itself-----------------------------------------------------------------------------------
#Capacités de l'assistant
SKILLS = ["fermer", "ouvrir", "chercher", "heure",  "lumière", "lire agenda"]

#Commandes pour exploiter ces capacités
COMMANDS = {
    "fermer" : ["laisse-moi", "ferme-toi", "arrête-toi"],
    "ouvrir" : ["ouvre", "ouvrir", "lancer", "lance", "démarrer", "démarre"],
    "heure" : ["quelle heure est-il", "il est quelle heure"],
    "lumière" : ["allume", "éteins"],
    "lire agenda": ["qu'est-ce que j'ai de prévu", "quel est le programme"],
    "chercher" : ["cherche sur youtube", "cherche sur internet", "cherche sur wikipedia", "recherche sur youtube", "recherche sur internet", "recherche sur wikipedia", "mets-moi sur youtube", "cherche", "recherche"]
}

#Comment appeller l'assistant
CALL_WORDS = ["assistant"]

#Ce que l'assistant peut répondre quand on le rappelle
LINES = ["Que puis-je faire pour vous ?", "Plaît-il ?", "Me voilà", "C'est bien moi, je vous écoute", "Je vous écoute"]


#--------------------------------------------------------------Config des applications que l'assistant peut ouvrir---------------------------------------------------------------------

#Applications connues
KNOWN_APPS = ["code", "brave", "discord", "wps", "workFile", "minecraft"]

#Alias des applications
APPS = {
    "code" : ["vscode", "visual studio", "code", "vs"],
    "brave" : ["brave", "internet"],
    "discord" : ["discord"],
    "wps" : ["wps", "word", "éditeur"],
    "workFile" : ["dossier travail", "travail"],
    "minecraft" : ["minecraft"]
}

#Chemins vers les applications
PATHS = {
    "code" : "D:\\programmes\\Microsoft VS Code\\Code.exe",
    "brave" : "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe",
    "discord" : "D:\\programmes\\Discord\\Update.exe --processStart Discord.exe",
    "wps" : "C:\\Users\\Administrateur\\AppData\\Local\\Kingsoft\\WPS Office\\ksolaunch.exe",
    "workFile" : 'explorer /select,"D:\\Travail\\"',
    "minecraft" : "D:\\Jeux\\Minecraft\\MinecraftLauncher.exe"
}

#Noms conviviaux des applications
NAMES = {
    "code" : "Visual Studio Code",
    "brave" : "Brave",
    "discord" : "Discord",
    "wps" : "WPS",
    "workFile" : "Dossier de Travail",
    "minecraft" : "Minecraft"
}


#----------------------------------------------------------------------Config de la recherche par l'assistant--------------------------------------------------------------------------

DDGO_SEARCH_TYPES = ["duckduckgo", "recherche"]


#----------------------------------------------------------------------------Config du calendrier--------------------------------------------------------------------------------------

DAYS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]

#------------------------------------------------------------------------------Config de la météo--------------------------------------------------------------------------------------

API_KEY = "" #Your api key for weatherbit
CITIES = {
    "Tours" : [47.38333, 0.68333]
}

#----------------------------------------------------------------------------Config des ampoules---------------------------------------------------------------------------------------

#Différentes ampoules que l'assistant peut contrôler
BULBS = ["spot chambre"]

#Table de correspondance entre le nom de l'ampoule et son IP
BULBS_IPS = {
    "spot chambre" : "192.168.0.136"
}

BULB_ROOMS = {
    "chambre" : ["spot chambre"]
}

ROOMS = ["chambre"]
