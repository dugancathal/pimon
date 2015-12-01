from multi_swipe import MultiSwipe
import pytest

from neopixels.pixel import Pixel
from utils import colors


class FakeStrip:
    def __init__(self):
        self.pixels = [Pixel(i, colors.black) for i in range(60)]

    def num_pixels(self):
        return len(self.pixels)

    def reset(self):
        pass

    def set_color_of(self, pixel_index, color):
        self.pixels[pixel_index].color = color

    def color_wipe(self, color, wait_ms=50, reverse_wipe=False):
        pass

    def show(self):
        pass

def fakesleep(self, amount=1):
    pass


class TestMultiSwipe:
    def setup(self):
        self.strip = FakeStrip()
        self.color_list = [colors.green, colors.red, colors.blue]
        self.swipe = MultiSwipe(self.strip, self.color_list, sleep=fakesleep)

    def test_strip_start_render(self):
        self.swipe.render_at(0)

        assert self.strip.pixels[0].color == colors.green
        assert self.strip.pixels[1].color == colors.black
        assert self.strip.pixels[20].color == colors.red
        assert self.strip.pixels[21].color == colors.black
        assert self.strip.pixels[40].color == colors.blue
        assert self.strip.pixels[41].color == colors.black

    def test_strip_render_tick_1(self):
        self.swipe.render_at(1)

        assert self.strip.pixels[0].color == colors.black
        assert self.strip.pixels[1].color == colors.green
        assert self.strip.pixels[2].color == colors.black
        assert self.strip.pixels[20].color == colors.black
        assert self.strip.pixels[21].color == colors.red
        assert self.strip.pixels[22].color == colors.black
        assert self.strip.pixels[40].color == colors.black
        assert self.strip.pixels[41].color == colors.blue
        assert self.strip.pixels[42].color == colors.black

    def test_strip_fill_renders_each_one(self):
        self.swipe.fill()

        for i in range(20):
            assert self.strip.pixels[i].color == colors.green
        for i in range(20, 40):
            assert self.strip.pixels[i].color == colors.red
        for i in range(40, 60):
            assert self.strip.pixels[i].color == colors.blue

    def test_strip_clear_at_tick0_clears_the_first_pixel_in_each_section(self):
        self.swipe.fill()
        self.swipe.clear_at(0)

        assert self.strip.pixels[0].color == colors.black
        assert self.strip.pixels[1].color == colors.green
        assert self.strip.pixels[20].color == colors.black
        assert self.strip.pixels[21].color == colors.red
        assert self.strip.pixels[40].color == colors.black
        assert self.strip.pixels[41].color == colors.blue

    def test_strip_empty_clears(self):
        self.swipe.fill()
        self.swipe.empty()

        for i in range(20):
            assert self.strip.pixels[i].color == colors.black
        for i in range(20, 40):
            assert self.strip.pixels[i].color == colors.black
        for i in range(40, 60):
            assert self.strip.pixels[i].color == colors.black
