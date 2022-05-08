class ObstacleSensor:
    """
        This class is an attempt to represent
        a obstacle sensor that works with
        LM393 IC.
    """
    
    
    def __init__(self, pin) -> None:
        """
            Get the sensor's OUT pin.
        """
        self.__infra = pin
        
    
    def __filter(self) -> bool:
        """
            Convert 1 or 0 to True or False.
        """
        value = self.__infra.value()
        new_value = False
        if value == 0:
            new_value = True
            
        return new_value
    
    
    def detected(self) -> bool:
        """
            Return if the sensor detect
            something.
        """
        value = self.__filter()
        return value
    
    
    def not_detected(self) -> bool:
        """
            Return if the sensor not detect
            somethin.
        """
        value = self.__filter()
        return (not value)