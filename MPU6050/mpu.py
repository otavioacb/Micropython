from machine import I2C
from time import sleep_ms
from math import atan2, pi

CONFIG = 0x1A
MPU_VALUES = 0x3B
GYRO_CONFIG = 0x1B
ACC_CONFIG = 0x1C
PWR_MGMT = 0x6B

GYRO_VALUES = {
    "0": [250, 131],
    "1": [500, 65.5],
    "2": [1000, 32.8],
    "3": [2000, 16.8]
}

ACC_VALUES = {
    "0": [2, 16384],
    "1": [4, 8192],
    "2": [8, 4096],
    "3": [16, 2048]
}

def bytes_to_int(hsb, lsb):
    if not hsb & 0x80:
        return hsb << 8 | lsb
    return -(((hsb ^ 255) << 8) | (lsb ^ 255) + 1)

class MPU6050:
    
    def __init__(self, scl, sda, addr=0x68, gyro_conf = 1, acc_conf = 0):
        self.__addr = addr
        self.__mpu = I2C(scl=scl, sda=sda)
        
        self.gyro_conf = GYRO_VALUES[str(gyro_conf)] 
        self.acc_conf = ACC_VALUES[str(acc_conf)]
        
        self.values = {"a_x": 0, "a_y": 0, "a_z": 0, "g_x": 0, "g_y": 0, "g_z": 0}
        self.offsets = {"a_x": 0, "a_y": 0, "a_z": 0, "g_x": 0, "g_y": 0, "g_z": 0}
        
        self.theta = 0
        self.phi = 0
        self.rho = 0
        
        self.wake()
        
    
    def wake(self):
        self.__mpu.start()
        self.__mpu.writeto_mem(self.__addr, PWR_MGMT, b'\x00')
        self.__mpu.stop()
        
        sleep_ms(50)
        
    
    def gyro_config(self, scale_range):
        if scale_range >= 0 and scale_range < 4:
            self.gyro_conf = GYRO_VALUES[str(scale_range)]
        else:
            print("Please, choose a scale value between 0 and 3")
            
    
    def acc_config(self, scale_range):
        if scale_range >= 0 and scale_range < 4:
            self.acc_conf = ACC_VALUES[str(scale_range)]
        else:
            print("Please, choose a scale value between 0 and 3")
        
    
    def calibrate(self, samples=10):
        for i in range(0, samples):
            sample = self.get_values()
            
            self.offsets["a_x"] += (sample["a_x"]/samples)
            self.offsets["a_y"] += (sample["a_y"]/samples)
            self.offsets["a_z"] += (sample["a_z"]/samples)
            self.offsets["g_x"] += (sample["g_x"]/samples)
            self.offsets["g_y"] += (sample["g_y"]/samples)
            self.offsets["g_z"] += (sample["g_z"]/samples)
        
        print("Calibration finished")
    
    def get_values(self):
        self.__mpu.start()
        raw_values = bytearray(self.__mpu.readfrom_mem(self.__addr, MPU_VALUES, 14))
        self.__mpu.stop()

        self.values["a_x"] = (bytes_to_int(raw_values[0], raw_values[1])/self.acc_conf[1]) - self.offsets["a_x"]
        self.values["a_y"] = (bytes_to_int(raw_values[2], raw_values[3])/self.acc_conf[1]) - self.offsets["a_y"]
        self.values["a_z"] = (bytes_to_int(raw_values[4], raw_values[5])/self.acc_conf[1]) - self.offsets["a_z"]

        self.values["g_x"] = (bytes_to_int(raw_values[8], raw_values[9])/self.gyro_conf[1]) - self.offsets["g_x"]
        self.values["g_y"] = (bytes_to_int(raw_values[10], raw_values[11])/self.gyro_conf[1]) - self.offsets["g_y"]
        self.values["g_z"] = (bytes_to_int(raw_values[12], raw_values[13])/self.gyro_conf[1]) - self.offsets["g_z"]
        
        return self.values


    def get_complimentary_values(self, dt):
        thetaG = self.values["g_y"]*dt
        phiG = self.values["g_x"]*dt
        rhoG = self.values["g_z"]*dt
        
        thetaA = atan2(self.values["a_x"], self.values["a_z"])
        phiA = atan2(self.values["a_y"], self.values["a_z"])
        rhoA = atan2(self.values["a_y"], self.values["a_x"])
    
        self.theta = ((self.theta+ thetaG)*0.85)+(thetaA*0.15)
        self.phi = ((self.phi + phiG)*0.85) + (phiA*0.15)
        self.rho = (((self.rho + rhoG)*0.85) + (rhoA*0.15))
         
        return (self.theta, self.phi, self.rho)