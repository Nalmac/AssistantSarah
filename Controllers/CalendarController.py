import datetime
import pytz

class CalendarController():
    def __init__(self, constants, service, assistant):
        self.constants = constants
        self.assistant = assistant
        self.service = service
        self.today = datetime.date.today()
        self.day = -1
        self.day_of_week = -1
        self.month = -1
        self.year = self.today.year


    def getDate(self, text):
        text = text.lower()
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
    
    def getDateExplicit(self, text):
        for word in text.split():
            if word in self.constants.MONTHS:
                self.month = self.constants.MONTHS.index(word) + 1
            elif word in self.constants.DAYS:
                self.day_of_week = self.constants.DAYS.index(word) + 1
            elif word.isdigit():
                self.day = int(word)
            elif word == "premier":
                self.day = 1


    def getEvents(self, day):
        
        (date, end_date) = self.processDate(day)

        events_finder = self.service.events()
        events_query = events_finder.list(calendarId='primary', timeMin=date, timeMax=end_date, singleEvents=True, orderBy='startTime')
        events_result = events_query.execute()
        events = events_result.get("items", [])

        self.processEvents(events)
        
    def processDate(self, day):
        date = datetime.datetime.combine(day, datetime.datetime.min.time())
        end_date = datetime.datetime.combine(date, datetime.datetime.max.time())

        utc = pytz.UTC
        date = date.astimezone(utc).isoformat()
        end_date = end_date.astimezone(utc).isoformat()

        return (date, end_date)
    
    def processEvents(self, events):
        if not events:
            self.assistant.speak("Vous n'avez rien de prévu")
        else:
            self.assistant.speak(f"Vous avez {len(events)} évènement prévus")
            for event in events:
                try:
                    start = event["start"].get('dateTime', event["start"].get("date"))
                    start_time = start.split("T")[1].split("+")[0]
                    start_time = start_time.split(":")[0] + " heures " + start_time.split(":")[1]
                    self.assistant.speak(event["summary"] + "à" + start_time)
                except:
                    self.assistant.speak(event["summary"])
    

    def handleCommand(self, cmd):
        day = self.getDate(cmd)
        self.getEvents(day)