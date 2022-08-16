import serial
import time

class Connection(object):
    def __init__(self, path,baud):
        self.path = path
        self.baud = baud
        self.ser = serial.Serial(path,baud)
        time.sleep(5)
        self.data = None
    
    def readData(self):
        self.ser.flushInput()
        txt = self.ser.readline()
        txt = txt.decode()
        txt = txt.rstrip()
        self.data = list(map(float, txt.split()))
        return self.data
    
    def getData(self):
        return self.data
    
    def getLightIntensity(self):
        return self.data[0]

    def getHumidity(self):
        return self.data[1]

    def getTempC(self):
        return self.data[2]

    def getTempF(self):
        return self.data[3]
    
    def getMoistureValue(self):
        return self.data[4]