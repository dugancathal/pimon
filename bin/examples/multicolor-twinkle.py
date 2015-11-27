import math
import time
import sys
from random import randrange as rand
from neopixel import *

FADE_RATE = 0.96

def randomPixelIndex(strip):
    return rand(strip.numPixels())

def randomRGB():
    return [ rand(255), rand(255), rand(255) ]

def randomColor():
    return Color(*randomRGB())

def faded(colorBit):
    return int(math.floor(colorBit * FADE_RATE))

def multicolorTwinkle(strip):
    pixels = list(range(strip.numPixels()))
    for i in range(strip.numPixels()):
        pixels[i] = randomRGB()

    if rand(0,20) == 1:
        i = randomPixelIndex(strip)
        pixels[i] = randomRGB()
        strip.setPixelColor(i, Color(*pixels[i]))

    for index, pixel in enumerate(pixels):
        if pixel[0] > 1 and pixel[1] > 1 and pixels[2] > 1:
            strip.setPixelColor(index, Color(*pixel))

            if pixel[0] > 1:
                pixels[index][0] = faded(pixel[0])
            else:
                pixels[index][0] = 0

            if pixel[1] > 1:
                pixels[index][1] = faded(pixel[1])
            else:
                pixels[index][1] = 0

            if pixel[2] > 1:
                pixels[index][2] = faded(pixel[2])
            else:
                pixels[index][2] = 0

	else:
	    strip.setPixelColor(index, Color(0, 0, 0))
    strip.show()
    time.sleep(0.1)

if __name__ == "__main__":
    LED_COUNT      = 60      # Number of LED pixels.
    LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
    LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    NUM_SECONDS=int(sys.argv[1])

    strip = Adafruit_NeoPixel(
        LED_COUNT,
        LED_PIN,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS
    )
    strip.begin()
    for i in range(NUM_SECONDS*100):
        multicolorTwinkle(strip)
    for i in reversed(range(strip.numPixels())):
        strip.setPixelColor(i, Color(0, 0, 0))
        time.sleep(0.1)
        strip.show()
