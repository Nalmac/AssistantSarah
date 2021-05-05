from Services.WeatherApiWrapper import ApiWrapper
from Services.DateConverter import TextDate, dateToText, dateFromDelta
import datetime

class WeatherController():
    def __init__(self, assistant):
        self.api = ApiWrapper()
        self.assistant = assistant
    
    def getCurrentWeather(self, city = "Tours", country = "FR"):
        weather_data = self.api.getCurrent(city=city, country=country)
        message = "Aujourd'hui à " + city + ", il fait " + str(weather_data["temp"])+ " degrès avec " + weather_data["weather"]
        self.assistant.speak(message)
    
    def getFutureWeather(self, city = "Tours", country = "FR", days = 2):
        weather_data = self.api.getFuture(city=city, country=country, days=days)
        date = "le " + dateToText(dateFromDelta(days)) if days > 2 else "Demain"
        message = date + " à " + city + ", il fait " + str(weather_data["temp"]) + " degrès avec " + weather_data["weather"]
        self.assistant.speak(message)

    def handleCommand(self, cmd):
        date = TextDate(cmd).toDate()
        if date is None or date == datetime.date.today():
            self.getCurrentWeather()
        else:
            delta = date - datetime.date.today()
            self.getFutureWeather(days=delta.days)      
        