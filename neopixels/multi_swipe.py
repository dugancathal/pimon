import time

from utils import colors


class MultiSwipe:
    def __init__(self, strip, color_list, sleep=time.sleep):
        self.sleep = sleep
        self.colors = color_list
        self.strip = strip
        self.section_length = int(self.strip.num_pixels() / len(self.colors))

    def step(self, times=1):
        for _ in range(times):
            self.fill()
            self.empty()

    def fill(self):
        for tick in range(self.section_length):
            self.render_at(tick)
            self.sleep(0.1)

    def empty(self):
        for tick in reversed(range(self.section_length)):
            self.clear_at(tick)
            self.sleep(0.1)

    def render_at(self, tick):
        for i, color in enumerate(self.colors):
            self.strip.set_color_of((i * self.section_length) + tick, color)
        self.strip.show()

    def clear_at(self, tick):
        for i, color in enumerate(self.colors):
            self.strip.set_color_of((i * self.section_length) + tick, colors.black)
        self.strip.show()
