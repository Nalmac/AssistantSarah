from yeelight import Bulb

class LightController():
    def __init__(self, constants):
        self.constants = constants
        self.bulbs = self.constants.BULBS
    
    def lightOn(self, bulb):
        ip = self.constants.BULBS_IPS[bulb]
        bulb = Bulb(ip)
        bulb.turn_on()
    
    def lightOff(self, bulb):
        ip = self.constants.BULBS_IPS[bulb]
        bulb = Bulb(ip)
        bulb.turn_off()

    def lightsOn(self, room):
        bulbs = self.constants.BULB_ROOMS[room]
        for i in bulbs:
            ip = self.constants.BULBS_IPS[i]
            bulb = Bulb(ip)
            bulb.turn_on()
    
    def lightsOff(self, room):
        bulbs = self.constants.BULB_ROOMS[room]
        for i in bulbs:
            ip = self.constants.BULBS_IPS[i]
            bulb = Bulb(ip)
            bulb.turn_off()
    
    def process(self, cmd):
        for i in self.constants.BULBS:
            if i in cmd.lower():
                if "allume" in cmd.lower():
                    self.lightOn(i)
                if "éteins" in cmd.lower():
                    self.lightOff(i)
                return True
            
        for i in self.constants.BULB_ROOMS:
            if i in cmd.lower():
                if "allume" in cmd.lower():
                    self.lightsOn(i)
                if "éteins" in cmd.lower():
                    self.lightsOff(i)
                return True
                 