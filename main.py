import time
import MatrixLED4Col
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

#Constants
RATCH = 3
SIK = 4
AnSI = 7
GrnSI = 8
RedSI = 9

LEDSIZE = 16

PutList = [
[0,0,0,0,0,0,0,0,0,0,0,0,6,6,0,0,],
[6,6,6,6,0,0,0,6,6,6,6,6,0,0,0,0,],
[0,0,0,6,0,0,0,0,0,0,6,0,0,0,0,0,],
[0,0,6,0,0,0,0,0,0,0,6,0,0,0,0,0,],
[0,0,6,0,0,0,0,6,0,0,6,0,0,0,0,0,],
[0,6,0,0,0,0,0,6,0,0,6,0,0,0,0,0,],
[0,6,6,6,6,0,0,6,0,0,6,6,6,0,0,0,],
[6,0,0,0,6,0,0,6,0,0,6,0,0,0,0,0,],
[0,0,0,0,6,0,0,6,0,0,6,0,0,0,0,0,],
[0,0,0,0,6,0,0,6,0,0,6,0,0,0,0,0,],
[6,0,0,6,0,0,0,6,0,0,6,0,0,0,0,0,],
[0,6,0,6,0,0,0,6,0,0,6,0,0,0,0,0,],
[0,0,6,0,0,6,6,6,6,6,0,6,6,6,0,0,],
[0,6,0,6,0,0,0,0,0,0,0,0,0,0,0,0,],
[6,0,0,0,6,6,0,0,0,0,0,0,0,0,0,0,],
[0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,0,],]

GPIO.setup(RATCH, GPIO.OUT)
GPIO.setup(SIK, GPIO.OUT)
GPIO.setup(AnSI, GPIO.OUT)
GPIO.setup(GrnSI, GPIO.OUT)
GPIO.setup(RedSI, GPIO.OUT)

MatrixLED = MatrixLED4Col.MatrixLED4Col(LEDSIZE, RATCH, SIK, AnSI, GrnSI, RedSI)

MatrixLED.flashLED()

try:
    time.sleep(2)
    error = MatrixLED.SetPtnList(PutList)
    print(error)
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    MatrixLED.loopFlag = False
    time.sleep(0.5)
    GPIO.cleanup()
