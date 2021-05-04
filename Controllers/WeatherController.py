from weatherbit.api import Api
import googletrans
import constants

class WeatherController():
    def __init__(self, constants, assistant):
        self.key = constants.API_KEY
        self.constants = constants
        self.api = Api(self.key)
        self.assistant = assistant
        self.api.set_granularity('daily')
        self.translator = googletrans.Translator()
    
    def getCurrentWeather(self, city = "Tours"):
        lat = self.constants.CITIES[city][0]
        lon = self.constants.CITIES[city][1]
        weather = self.api.get_forecast(lat=lat, lon=lon, lang="fr")
        today = weather.get_series(["min_temp", "max_temp", "temp", "weather"])[0]
        
        maxTemp = today["max_temp"]
        minTemp = today["min_temp"]
        temp = today["temp"]
        weather_en = today["weather"]["description"]
        print(weather_en)
        print(self.translator)
        weather = self.translator.translate(weather_en, dest='la')
        print(f"Aujourd'hui à {city}, il fait {temp} degrès avec {weather}. La température minimale est de {minTemp} et la maximale de {maxTemp}")

assistant = ""
controller = WeatherController(constants,  assistant)
controller.getCurrentWeather()