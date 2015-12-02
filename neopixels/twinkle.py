import time
from random import randrange as rand

from utils.colors import Color, gray


class Twinkle:
    def __init__(self, strip):
        self.strip = strip

    def random_pixel_index(self):
        return rand(self.strip.num_pixels())

    def step(self, times=1):
        for i in range(times):
            self.render()

    def render(self):
        twinklers = [self.strip.random_pixel() for _ in range(rand(15))]
        for pixel in twinklers:
            pixel.set_color(gray)
        self.strip.show()
        for i in range(0, 5):
            self.fade(i, twinklers)
        for i in reversed(range(0, 6)):
            self.fade(i, twinklers)
        self.strip.reset()

    def fade(self, i, pixels):
        for index, pixel in enumerate(pixels):
            r = pixel.red() * (i+1)
            r /= 5
            g = pixel.green() * (i+1)
            g /= 5
            b = pixel.blue() * (i+1)
            b /= 5
            self.strip.strip.setPixelColor(pixel.index, Color(int(r), int(g), int(b)).to_i())
        self.strip.strip.show()
        time.sleep(0.05)
