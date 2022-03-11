from motor import Motor
from math import fabs

class CreateMotor():
    """
        This class will create a DC Motor
        with Motor class specifications.
    """
    
    
    def __init__(self, name, pin_pwm, pin_dir):
        """
            Define a motor with a name, pwm pin and
            direction pin.
        """
        self.__name = name
        self.__gpio = [pin_pwm, pin_dir]
        self.__motor = Motor(pin_pwm, pin_dir)
        
    def __repr__(self):
        """
            Return a representation of CreateMotor object.
        """
        return self.__motor.__repr__
    
    def __str__(self):
        """
            Return a piece of information about CreateMotor object.
        """
        msg = self.__name + ": plugged in PWM GPIO " + str(self.__gpio[0]) + " and GPIO" + str(self.__gpio[1]) + "."
        return msg
        
    def speed(self, value):
        """
            Controll PWM pin value to measure Motor speed
            with negative and positive values.
        """
        try:
            if value > 0:
                self.__motor.dir(0)
                self.__motor.spd(value)
            elif value < 0:
                self.__motor.dir(1)
                self.__motor.spd(fabs(value))
            else:
                self.__motor.spd(0)
        except e:
            print(e)
