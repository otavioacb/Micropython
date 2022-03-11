from led import Led
from time import sleep

class ControlLed():
    """
        This class is a to implement
        some actions with the LEDs.
    """
    def __init__(self):
        self.__led = Led()
        
    
    def on(self):
        """
            Turn on all LEDs.
        """
        self.__led.shift("11111111")
    
    
    def off(self):
        """
            Turn off all LEDs.
        """
        self.__led.shift("00000000")
        
        
    def blink(self, byte, time):
        """
            Turn on and turn off the LEDs
            informed for specific gape of time.
        """
        self.__led.shift(byte)
        sleep(time)
        self.__led.shift("00000000")
        sleep(time)
        
        
