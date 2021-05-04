import requests
import constants

class ApiWrapper():
    def __init__(self):
        self.base_url = constants.BASE_URL
        self.key = constants.API_KEY
        self.lang = "fr"
        self.cities = constants.CITIES
        self.key = constants.API_KEY
    
    def getCurrent(self, city = "Tours", country = "FR"):
        params = {
            "postal_code" : self.cities[city], 
            "country" : country, 
            "lang" : self.lang, 
            "key" : self.key
        }
        
        url = self.base_url + "current"
        response = requests.get(url, params=params)
        data = response.json()["data"][0]
        return {
            "weather" : data["weather"]["description"],
            "temp" : data["temp"]
        }
    
    def getFuture(self, city = "Tours", country = "FR", days = 2):
        params = {
            "postal_code": self.cities[city],
            "country": country,
            "lang": self.lang,
            "key": self.key,
            "days": days,
        }

        url  = self.base_url + "forecast/daily"
        response = requests.get(url, params=params)
        data = response.json()["data"][-1]
        return {
            "weather" : data["weather"]["description"],
            "temp" : data["temp"]
        }