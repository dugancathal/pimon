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

def twinkle(strip):
    pixels = list(range(strip.numPixels()))
    for i in range(strip.numPixels()):
        pixels[i] = [10, 10, 10]

    index = randomPixelIndex(strip)
    twinklers = [None for i in range(rand(5))]
    for i, _ in enumerate(twinklers):
        randomIndex = randomPixelIndex(strip)
        twinklers[i] = [randomIndex, pixels[randomIndex]]

    for i in range(0, 5):
        for index, pixel in twinklers:
            r = pixel[0] * (i + 1); r /= 5
            g = pixel[1] * (i + 1); g /= 5
            b = pixel[2] * (i + 1); b /= 5
            strip.setPixelColor(index, Color(int(r), int(g), int(b)))
        strip.show()
        time.sleep(0.05)
    for i in reversed(range(0, 6)):
        for index, pixel in twinklers:
            r = pixel[0] * (i); r /= 5
            g = pixel[1] * (i); g /= 5
            b = pixel[2] * (i); b /= 5
            strip.setPixelColor(index, Color(int(r), int(g), int(b)))
        strip.show()
        time.sleep(0.05)

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
        twinkle(strip)
    for i in reversed(range(strip.numPixels())):
        strip.setPixelColor(i, Color(0, 0, 0))
        time.sleep(0.1)
        strip.show()
