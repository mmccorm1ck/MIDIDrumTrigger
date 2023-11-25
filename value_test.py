import time
import board
import analogio
import digitalio
#import usb_midi
#import adafruit_midi
#from adafruit_midi.note_off import NoteOff
#from adafruit_midi.note_on import NoteOn
#from adafruit_simplemath import map_range

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

adc = analogio.AnalogIn(board.A0)

#usb_midi = adafruit_midi.MIDI(
#    midi_out=usb_midi.ports[1],
#    out_channel=0
#    )

def ledOn():
    led.value = True

def ledOff():
    led.value = False

val = 0
maxval = 0
total = 0
length = 0
x = 0

weighting = 2000

while True:
    val = adc.value
    while val > 700:
        length = length + 1
        total = total + (val / 1000)
        if val > maxval:
            maxval = val
        val = adc.value
        if val <= 700:
            ledOn()
            x = total / length
            if x > 127:
                x = 127
            print(x)
            maxval = 0
            length = 0
            x = 0
            time.sleep(0.02)
            ledOff()