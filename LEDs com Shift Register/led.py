from machine import Pin
from time import sleep

class Led():
    """
        This class is an attempt to represent
        a connection with IC who controll all
        circuits' LEDs.
    """
    def __init__(self):
        self.__data = Pin(15, Pin.OUT)
        self.__latch = Pin(12, Pin.OUT)
        self.__clock = Pin(14, Pin.OUT)
        
        
    def shift(self, data):
        """
            Set up pin states to send bit by bit
            for the shift register.
        """
        
        # Latch LOW -> start data sending
        self.__clock.value(0)
        self.__latch.value(0)
        self.__clock.value(1)
        
        # Catch each bit in reverse order
        for bit in range(7, -1, -1):
            self.__clock.value(0)
            self.__data.value(int(data[bit]))
            self.__clock.value(1)
            
        # Latch HIGH -> finish data sending
        self.__clock.value(0)
        self.__latch.value(1)
        self.__clock.value(1)
        
    