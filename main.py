import time
import MatrixLED2^2Col

#Constants
LEDSIZE = 16 
DummyPtnList = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
#0=K, 2=Grn, 3=Red, 6=Org

MatrixLED = MatrixLED2^2Col(LEDSIZE, "RED", "GREEN")

MatrixLED.push(DummyPtnList)
MatrixLED.flashLED()

try:
    while True:
        time.sleep(0.1)

except KeyboardInterrupt:
    MatrixLED.Loop = False


