import RPi.GPIO as GPIO
import time
import threading


class MatrixLED4Col():
    def __init__(self, SIZE, RATCH, SIK, AnSI, GrSI, ReSI):
        self.SIZE = SIZE
        self.RATCH = RATCH
        self.SIK = SIK

        self.AnSI = AnSI
        self.GrSI = GrSI
        self.ReSI = ReSI

        self.ReList = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],]
        self.GrList = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],]


    def SetSI(self, SI, DATA):
        if DATA == 1:
            GPIO.output(SI, GPIO.LOW)
        elif DATA == 0:
            GPIO.output(SI, GPIO.HIGH)
        return

    def Clock(self, PIN):
        GPIO.output(PIN,GPIO.HIGH)
        GPIO.output(PIN,GPIO.LOW)
        return

    def flashLED(self):
        AnDATA = 0
        for a in range(0,4):
            for x in range(0,self.SIZE):
                for y in range(0, self.SIZE):
                    if x == y:
                        AnDATA = 0
                    else:
                        AnDATA = 1

                    SetSI(self.AnSI, AnDATA)
                    SetSI(self.GrSI, (self.GrList[x] >> y) & 0b1)
                    SetSI(self.ReSI, (self.ReList[x] >> y) & 0b1)
                
                Clock(self.SIK)
            Clock(self.RATCH)
