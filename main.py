import time
import MatrixLED4Col

#Constants
LEDSIZE = 16 
DummyPtnList = [[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6],[6]]
#0=K, 2=Grn, 3=Red, 6=Org

MatrixLED = MatrixLED4Col(LEDSIZE, "RED", "GREEN")

MatrixLED.push(DummyPtnList)
MatrixLED.flashLED()

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    MatrixLED.Loop = False


