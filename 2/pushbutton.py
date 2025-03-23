import time, random
import board, neopixel, rainbowio
from digitalio import DigitalInOut, Direction, Pull

num_leds = 6

leds = neopixel.NeoPixel(board.GP19, num_leds, brightness=0.4, auto_write=False )

delta_hue = 256//num_leds
speed = 10  # higher numbers = faster rainbow spinning
i=0

leds.direction = Direction.OUTPUT

switch = DigitalInOut(board.GP18)
switch.direction = Direction.INPUT
switch.pull = Pull.UP


while True:   
    # We could also do "led.value = not switch.value"!
    if switch.value:
        print(switch.value)
        leds.value = False
    else:
        print(switch.value)
        leds.value = True
        for l in range(len(leds)):
            leds[l] = rainbowio.colorwheel( int(i*speed + l * delta_hue) % 255  )
            leds.show()  # only write to LEDs after updating them all
            i = (i+1) % 255
            time.sleep(0.01)

    #time.sleep(0.01)  # debounce delay
