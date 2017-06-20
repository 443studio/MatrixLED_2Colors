import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BCM)

class MatrixLED4Col:
    def __init__(self, SIZE, RATCH, SIK, AnSI, GrSI, ReSI):
        self.SIZE = SIZE
        self.RATCH = RATCH
        self.SIK = SIK

        self.AnSI = AnSI
        self.GrSI = GrSI
        self.ReSI = ReSI

        self.AnDATA = 0

        self.loopFlag = True

        self.ReList = [
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],
[0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,],]
        self.GrList = [
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,],
[0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,],
[0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,],
[0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,],
[0,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,],
[0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,]]


    def SetSI(self, SI, DATA):
        if DATA:
            GPIO.output(SI, GPIO.HIGH)
        else:
            GPIO.output(SI, GPIO.LOW)

    def Clock(self, PIN):
        GPIO.output(PIN,GPIO.HIGH)
        GPIO.output(PIN,GPIO.LOW)
    def flashLED(self):
        for a in range(0,4):
            for x in range(0,self.SIZE):
                for y in range(0, self.SIZE):
                    if x == y:
                        self.AnDATA = 1
                    else:
                        self.AnDATA = 0

                    self.SetSI(self.AnSI, self.AnDATA)
                    self.SetSI(self.GrSI, not self.GrList[x][y])
                    self.SetSI(self.ReSI, not self.ReList[x][y])
                    self.Clock(self.SIK)
                self.Clock(self.RATCH)
                time.sleep(0.00000000000000000001)

        if self.loopFlag:
            t = threading.Thread(target=self.flashLED)
            t.start()
