import math
import time
import sys
from neopixel import *

class Scheme:
    def __init__(self, colors, count):
        self.colors = colors
        self.count = count

def remapNum(num, in_min, in_max, out_min, out_max):
    return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def gradientColor(scheme, iRange, gradRange, i):
    curRange = int(i / iRange)
    rangeIndex = int(i % iRange)
    colorIndex = int(rangeIndex / gradRange)
    start = (colorIndex % scheme.count)
    theEnd = ((colorIndex + 1) % scheme.count)
    if curRange % 2 != 0:
        start = scheme.count - 1 - start
        theEnd = scheme.count - 1 - theEnd

    return [
        remapNum(rangeIndex % gradRange, 0, gradRange, scheme.colors[start][0], scheme.colors[theEnd][0]),
        remapNum(rangeIndex % gradRange, 0, gradRange, scheme.colors[start][1], scheme.colors[theEnd][1]),
        remapNum(rangeIndex % gradRange, 0, gradRange, scheme.colors[start][2], scheme.colors[theEnd][2])
    ]

def gradient(strip, scheme, repeat, speedInMS):
    iRange = int(math.ceil(strip.numPixels() / repeat))
    gradRange = int(math.ceil(iRange / 2))

    t = int(time.time()*1000)
    offset = t / speedInMS if speedInMS > 0 else 0
    
    oldColor = gradientColor(scheme, iRange, gradRange, strip.numPixels()-1+offset)
    for i in range(strip.numPixels()):
        currentColor = gradientColor(scheme, iRange, gradRange, i+offset)
        if speedInMS > 0:
            strip.setPixelColor(
                i,
                Color(
                    remapNum(t % speedInMS, 0, speedInMS, oldColor[0], currentColor[0]),
                    remapNum(t % speedInMS, 0, speedInMS, oldColor[1], currentColor[1]),
                    remapNum(t % speedInMS, 0, speedInMS, oldColor[2], currentColor[2])
                )
            )
        else:
            strip.setPixelColor(
                i,
                Color(
                    currentColor[0],
                    currentColor[1],
                    currentColor[2]
                )
            )
        oldColor = currentColor
    strip.show()

schemes = {
	"christmas": Scheme([[255, 0, 0], [0, 255, 0]], 2),
	"rgb": Scheme([[255, 0, 0], [0, 255, 0], [0, 0, 255]], 3),
        "hanukkah": Scheme([[0, 0, 255], [255, 255, 255]], 2),
        "rainbow": Scheme([[255, 0, 0], [255, 128, 0], [255, 255, 0], [0, 255, 0], [0, 0, 255], [128, 0, 255], [255, 0, 255], [255, 255, 255]], 8),
        "fire": Scheme([[255, 0, 0], [255, 102, 0], [255, 192, 0]], 3),
}
if __name__ == "__main__":
    LED_COUNT      = 60      # Number of LED pixels.
    LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
    LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

    NUM_SECONDS=int(sys.argv[1])
    SCHEME_NAME=sys.argv[2]

    strip = Adafruit_NeoPixel(
        LED_COUNT,
        LED_PIN,
        LED_FREQ_HZ,
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS
    )
    strip.begin()
    for i in range(NUM_SECONDS*10):
        gradient(strip, schemes[SCHEME_NAME], 6, 100)
        time.sleep(0.1)
    for i in reversed(range(strip.numPixels())):
        strip.setPixelColor(i, Color(0, 0, 0))
        time.sleep(0.1)
        strip.show()
