from createMotor import CreateMotor
import time

class ControlMotor():
    """
        This class is a attempt to simplify motor controls
        from CreateMotor class.
        
        Positive values will move robot forward.
        Negative values will move robot back.
    """
    
    
    def __init__(self):
        """
            Create DC Motor A and DC Motor B to control
            the robot's moviments.
        """
        self.__motorA = CreateMotor("Motor A", 5, 0)
        self.__motorB = CreateMotor("Motor B", 4, 2)
        
        
    def controlA(self, speed_a):
        """
            Pass speed value just for Motor A.
        """
        self.__motorA.speed(speed_a)


    def controlB(self, speed_b):
        """
            Pass speed value just for Motor B.
        """
        self.__motorB.speed(speed_b)


    def controlAll(self, speed_a, speed_b):
        """
            Pass speed value for all motors.
        """
        self.__motorA.speed(speed_a)
        self.__motorB.speed(speed_b)
