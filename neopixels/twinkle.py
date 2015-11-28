import time
from random import randrange as rand

from utils.colors import Color


class Twinkle:
    FADE_RATE = 0.96

    def __init__(self, strip):
        self.strip = strip

    def random_pixel_index(self):
        return rand(self.strip.num_pixels())

    def step(self):
        twinklers = [self.strip.random_pixel() for _ in range(rand(15))]
        for i in range(0, 5):
            self.fade(i, twinklers)
        for i in reversed(range(0, 6)):
            self.fade(i, twinklers)

    def fade(self, i, pixels):
        for index, pixel in enumerate(pixels):
            r = pixel.red() * i
            r /= 5
            g = pixel.green() * i
            g /= 5
            b = pixel.blue() * i
            b /= 5
            pixel.set_color(Color(int(r), int(g), int(b)))
        self.strip.show()
        time.sleep(0.05)
