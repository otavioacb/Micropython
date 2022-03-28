from machine import Pin, time_pulse_us
from time import sleep_us, ticks_us, ticks_diff


SOUND_SPEED = 0.000340 # m/us
PULSE_TIME = 10 # us
ECHO_TIMEOUT = 23530 # us
UNITS = ["cm", "m", "mm"] # allowed units


class HCSR04:
    """
        HCSR04 is a class to represent a
        hc-sr04 ultrassonic sensor and make easy
        to calculate the distance.
    """
    
    
    def __init__(self, trigger, echo, unit="m") -> None:
        """
            Set up trigger and echo pins.
            Define an unit of length.
        """
        self.__trig = Pin(trigger, Pin.OUT)
        self.__echo = Pin(echo, Pin.IN)
        self.__unit = unit.lower()

        # Making sure the sensor will
        # not receive any pulse rigth now
        self.__trig.value(0)
        

    def __pulse_out(self) -> None:
        """
            Send the wake up pulse for 10 microseconds.
        """
        self.__trig.value(1)
        sleep_us(PULSE_TIME)
        self.__trig.value(0)
        
    
    @property
    def unit(self) -> str:
        """
            Check the current unit of length.
        """
        return self.__unit
    
    
    @unit.setter
    def unit(self, unit) -> None:
        """
            Set an new unit of length
        """
        if unit in UNITS:
            self.__unit = unit.lower()
        else:
            raise BaseException("Invalid unit of length")
    
    
    def __convert(self, distance) -> float:
        """
            Convert the value in meter to
            other unit.
        """
        new_distance = 0
        print(distance)
        if self.__unit == "cm":
            new_distance = distance * 100
        elif self.__unit == "mm":
            new_distance = distance * 1000
        else:
            new_distance = distance
            
        return new_distance
            
        
    def distance(self) -> float:
        """
            Calculate the distance and
            return in the specified unit.
        """
        self.__pulse_out()
        time = time_pulse_us(self.__echo, 1, ECHO_TIMEOUT)
        
        distance = ((time * SOUND_SPEED) / 2)
        distance_formated = self.__convert(distance)
        
        return distance_formated