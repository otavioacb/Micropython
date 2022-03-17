from machine import Pin, PWM


class ServoMotor:
    """
        This class is an attempt to represent
        a PWM connection between microcontrollers
        and servo motors.
    """
    
    def __init__(self, pin) -> None:
        """
            Create a PWM connection with 50Hz.
        """
        
        self.__pwm = PWM(pin, freq=50)
        self.__angle = 0
        self.__duty = 0
        
    
    def __map(self) -> int:
        """
            Scale the angle values between 0 and 180 to
            40 and 115.
        """
        
        in_min, in_max = (0, 180)
        out_min, out_max = (40, 115)
        
        return int((self.__angle - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    
    
    @property
    def angle(self) -> int:
        """
            Return the servo's angle.
        """
        
        return self.__angle
    
    
    @angle.setter
    def angle(self, angle) -> None:
        """
            Set a new angle.
        """
        
        if angle >= 0 and angle <= 180:
            self.__angle = angle
            self.__duty = int(self.__map())
            self.__pwm.duty(self.__duty)
        else:
            return "Invalid angle. Set an angle between 0° and 180°."