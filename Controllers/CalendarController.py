import datetime
import pytz
from Services.DateConverter import TextDate

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
        day = TextDate(cmd).toDate()
        self.getEvents(day)