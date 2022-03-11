from machine import Pin,PWM

class Motor:
    """
        This class is an attempt to represent
        a DC Motor for ESP8266 to controll
        its movements.
        
        Pwm Pin -> Controll the motor speed.
        Dir Pin -> Controll the motor direction.
    """
    
    
    def __init__(self, pin_pwm, pin_dir):
        """
            Accepts a pwm pin value and direction pin value.
        """
        self.__pwm = PWM(Pin(pin_pwm), freq=1000, duty = 0)
        self.__dir= Pin(pin_dir, Pin.OUT)
   
   
    def __repr__(self):
       return "<Motor object>"
   
   
    def spd(self, value):
        """
            Accepts a speed value to controll the DC Motor.
        """
        self.__pwm.duty(value)


    def dir(self, direction = 0):
        """
            Accepts a direction value to controll the DC Motor.
        """
        if direction == 1:
            self.__dir.off()
        elif direction == 0:
            self.__dir.on()
        else:
            print("Error! Please, inform just 1 or 0 as direction value.")
