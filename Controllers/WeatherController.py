from Services.WeatherApiWrapper import ApiWrapper
from Services.DateConverter import TextDate

class WeatherController():
    def __init__(self, assistant):
        self.api = ApiWrapper()
        self.assistant = assistant
    
    def getCurrentWeather(self, city = "Tours", country = "FR"):
        weather_data = self.api.getCurrent(city=city, country=country)
        message = f"Aujourd'hui à {city}, il fait {weather_data["temp"]} degrès avec {weather_data["weather"]}."
        assistant.speak(message)
    
    def getFutureWeather(self, city = "Tours", country = "FR", days = 2):
        weather_data = self.api.getFuture(city=city, country=country, days=days)