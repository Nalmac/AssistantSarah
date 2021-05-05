import datetime
import pytz
import constants

class TextDate():
    def __init__(self, text):
        self.today = datetime.date.today()
        self.day = -1
        self.day_of_week = -1
        self.month = -1
        self.year = self.today.year
        self.text = text
    
    def toDate(self):
        text = self.text.lower()
        if self.getDateClose(text) is not None:
            return self.getDateClose(text)
        
        self.getDateExplicit(text)

        if self.month < self.today.month and self.month >= 1:
            year += 1

        if self.day < self.today.day and self.day >= 1:
            month += 1

        if self.month == -1 and self.day == -1 and self.day_of_week >= 0:
            return self.getDateFromWeekday(self.day_of_week)
        
        if self.month == -1 or self.day == -1:
            return None

        return datetime.date(self.year, self.month, self.day)
    
    def getDateExplicit(self, text):
        for word in text.split():
            if word in constants.MONTHS:
                self.month = constants.MONTHS.index(word) + 1
            elif word in constants.DAYS:
                self.day_of_week = constants.DAYS.index(word) + 1
            elif word.isdigit():
                self.day = int(word)
            elif word == "premier":
                self.day = 1
    
    def getDateClose(self, text):
        if "aujourd'hui" in text:
            return self.today
        elif "demain" in text:
            return self.today + datetime.timedelta(days=1)
        elif "après-demain" in text:
            return self.today + datetime.timedelta(days=2)

    def getDateFromWeekday(self, day_of_week):
        current_day_of_week = self.today.weekday()
        dif = day_of_week - current_day_of_week
        if dif < 0:
            dif += 7
            if "prochain" in text:
                dif += 7
        return today + datetime.timedelta(dif)

def dateToText(date):
    day = date.day
    month = constants.MONTHS[date.month - 1]
    dayText = "premier" if day == 1 else str(day)
    return str(day) + " " + month

def dateFromDelta(delta):
    today = datetime.date.today()
    delta = datetime.timedelta(days=delta)
    return today + delta