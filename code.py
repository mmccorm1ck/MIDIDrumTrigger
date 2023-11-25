import time
import board
import analogio
import digitalio
import usb_midi
import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

usb_midi = adafruit_midi.MIDI(
    midi_out=usb_midi.ports[1],
    out_channel=0
    )

def noteOn():
    led.value = True
    usb_midi.send(NoteOn(35,127))

def noteOff():
    usb_midi.send(NoteOff(35,0))
    led.value = False

adc = analogio.AnalogIn(board.A0)

while True:
    val = adc.value
    if val > 700:
        noteOn()
        while val > 700:
            val = adc.value
        time.sleep(0.02)
        noteOff()