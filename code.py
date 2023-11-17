import time
import board
import busio
from simpleio import map_range
from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
import usb_midi
import adafruit_midi

USB_MIDI_channel = 1
usb_midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=USB_MIDI_channel - 1)

pins = [26, 27]
leds = [15, 16]

thresh = 50

def sendNote(pin, vel):
    usb_midi.send(NoteOn(36+pin, ((vel+1)/8)-1))
    time.sleep(0.01)
    usb_midi.send(NoteOff(36+pin, 0))

def monitorPin(pinNo):
    max = AnalogIn(pins[pinNo])
    if max < thresh:
        return
    sent = False
    peak = False
    while True:
        newVal = AnalogIn(pins[pinNo])
        if newVal > max:
            max = newVal
        elif newVal > 1000:
            leds[pinNo].value = True
            peak = True
        elif newVal <1000 and peak == True:
            leds[pinNo].value = False
        elif newVal < max * 0.95 and sent == False:
            sendNote(pinNo, max)
            sent = True
        elif newVal < thresh and sent == True:
            return
    
while True:
    monitorPin(0)
    monitorPin(1)