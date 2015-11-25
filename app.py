import requests
import sys
import time

from neopixel import *

class BuildMapper:
    color_map = {
            "failed": Color(255, 0, 0),
            "fixed": Color(0, 255, 0),
            "success": Color(0, 255, 0),
            "running": Color(255, 255, 0),
            "not_run": Color(0, 0, 0)
    }
    def __init__(self, status):
        self.status = status

    def to_color(self):
        return self.color_map.get(self.status, self.color_map["not_run"])

class NeopixelStrip:
    LED_COUNT      = 60      # Number of LED pixels.
    LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
    LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

    def __init__(self):
        self.direction = 'forward'
        self.strip = Adafruit_NeoPixel(
            self.LED_COUNT,
            self.LED_PIN,
            self.LED_FREQ_HZ,
            self.LED_DMA,
            self.LED_INVERT,
            self.LED_BRIGHTNESS
        )
        self.strip.begin()

    def colorWipe(self, color, wait_ms=50):
        for i in self.iterator():
            self.setColorOf(i, color)
            time.sleep(wait_ms/1000.0)

    def iterator(self):
        if self.direction == 'backward':
            return reversed(range(self.numPixels()))
        else:
            return range(self.numPixels())
    def flipFlop(self):
        if self.direction == 'backward':
            self.direction = 'forward'
        else:
            self.direction = 'backward'

    def numPixels(self):
        return self.strip.numPixels()

    def setColorOf(self, pixelIndex, color):
        self.strip.setPixelColor(pixelIndex, color)
        self.strip.show()

    def reset(self):
        for i in range(self.numPixels()):
            self.setColorOf(i, Color(0, 0, 0))

class CircleCiBuildFetcher():
    api_url="https://circleci.com/api/v1"
    def __init__(self, project, token):
        self.project_endpoint = "%(url)s/project/%(project)s" % {"url": self.api_url, "project": project}
        self.token = token

    def builds(self):
        return requests.get(
            self.project_endpoint, 
            params={"circle-token": self.token, "limit": 5}, 
            headers={"Accept": "application/json"}
        ).json()

if __name__ == "__main__":
    strip = NeopixelStrip()
    circle_token = sys.argv[1]
    fetcher = CircleCiBuildFetcher("TruHearing/echo", circle_token)

    for index, build in enumerate(fetcher.builds()):
        rgb = BuildMapper(build["status"]).to_color()
        strip.colorWipe(rgb)
        strip.flipFlop()
    strip.reset()

