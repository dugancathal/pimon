import time
import sys
from random import randrange as rand
from neopixel import *

FADE_RATE = 0.96

def randomPixelIndex(strip):
    return rand(strip.numPixels)

def randomRGB():
    return [ rand(255), rand(255), rand(255) ]

def randomColor():
    return Color(*randomRGB())

def faded(colorBit):
    return colorBit * FADE_RATE

def twinkle(strip):
    pixels = []
    for i in range(strip.numPixels()):
        pixels[i] = randomRGB()

    if rand(0,20) == 1:
        i = randomPixelIndex(strip)
        pixel[i] = randomRGB()
        strip.setPixelColor(i, Color(*pixel[i]))

    for index, pixel in enumerate(range(strip.numPixels())):
        if pixels[i][0] > 1 && pixels[i][1] > 1 && pixels[i][2] > 1:
            strip.setPixelColor(i, Color(*pixel[i]))

        if pixel[i][0] > 1:
            pixel[i] = faded(pixel[i])
        else:
            pixel[i][0] = 0

        if pixel[i][1] > 1:
            pixel[i] = faded(pixel[i])
        else:
            pixel[i][1] = 0

        if pixel[i][2] > 1:
            pixel[i] = faded(pixel[i])
        else:
            pixel[i][2] = 0

    strip.show()
    time.sleep(0.01)

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
