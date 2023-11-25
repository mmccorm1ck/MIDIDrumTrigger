import time
import board
import busio
import analogio

val = 0
adc = analogio.AnalogIn(board.A0)
while True:
    val = adc.value
    if val > 500:
        print(val)
    time.sleep(0.0001)