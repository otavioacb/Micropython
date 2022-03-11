from machine import PWM, Pin

class RGB:
    """
        RGB class will simplify the mode as we use
        the RGB module with ESP. Here we can easily
        modify the values for each pin and also change
        the module's frequency.
    """
    
    
    def __init__(self, p_red, p_green, p_blue, freq=1000, duty=0):
        """
            Create 3 PWM pins for each pin of the RGB module.
        """
        self.__red = PWM(Pin(p_red), freq=freq, duty=duty)
        self.__green = PWM(Pin(p_green), freq=freq, duty=duty)
        self.__blue = PWM(Pin(p_blue), freq=freq, duty=duty)
        
        
    def colors(self, red, green, blue):
        """
            Change the value of each color individual. But
            first it is necessary to check if the value is
            grater than 0 and lesser than 255.
        """
        red = self.__check_value(red)
        green = self.__check_value(green)
        blue = self.__check_value(blue)
        
        self.__red.duty(red)
        self.__green.duty(green)
        self.__blue.duty(blue)
        
    
    def freq(self, value):
        """
            Enable the blink option for the module.
            Small frequency meaning slower blink. Therefore
            large frequency meaning faster blink.
        """
        self.__red.freq(value)
        self.__green.freq(value)
        self.__blue.freq(value)
        
        
    def __check_value(self, value):
        if value > 255:
            return 255
        elif value < 0:
            raise NameError("Invalid value for RGB module")
        else:
            return value
        
        
