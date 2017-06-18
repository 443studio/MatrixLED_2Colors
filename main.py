import time
import MatrixLED4Col
import RPi.GPIO as GPIO

#Constants
RATCH = 3
AnSIK = 4
GrnSIK = 5
RedSIK = 6
AnSI = 7
GrnSI = 8
RedSI = 9

LEDSIZE = 16


DummyPtnList = [[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6]]
#0=K, 2=Grn, 3=Red, 6=Org

MatrixLED = MatrixLED4Col(LEDSIZE, RATCH, SIK = [AnSIK,GrnSIK,RedSIK], SI = [AnSI, GrnSI, RedSI])

MatrixLED.push(DummyPtnList)
MatrixLED.flashLED()

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    MatrixLED.Loop = False


