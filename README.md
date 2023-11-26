## MIDI drum trigger module

A simple module to convert the audio signal from a drum trigger into USB MIDI messages. It is written in Circuitpython and designed to run on a Raspberry Pi Pico.

## Installation

Download the appropriate .UF2 file for your board from https://circuitpython.org/downloads and load it onto your device. Then simply copy code.py into the root directory. You will also need the adafruit_midi library from https://github.com/adafruit/Adafruit_CircuitPython_Bundle.

## Input stage

I used an Alesis Nitro Mesh drum trigger, which outputs audio from an internal contact microphone. This requires an input stage to make the signal usable and to avoid damage to the Pico. I decided to make it as simple as possible using the passive design shown below:
![InputStage.PNG]


## Warning

The specific component values used in the input stage were chosen for the type of trigger I used. If you use something different you may also need to modify the design to avoid damaging your microcontroller or trigger.
