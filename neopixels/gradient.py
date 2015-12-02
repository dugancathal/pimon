import math
import time

from utils.colors import Color


def remap_color(num, in_min, in_max, color_min, color_max):
    return Color(
        (num - in_min) * (color_max.red - color_min.red) / (in_max - in_min) + color_min.red,
        (num - in_min) * (color_max.green - color_min.green) / (in_max - in_min) + color_min.green,
        (num - in_min) * (color_max.blue - color_min.blue) / (in_max - in_min) + color_min.blue
    )


class Gradient:
    def __init__(self, strip, scheme, repetitions, speed):
        self.scheme = scheme
        self.repetitions = repetitions
        self.strip = strip
        self.speed = speed
        self.index_range = self.compute_index_range()
        self.gradient_range = self.compute_gradient_range()

    def smooth_color_over_range(self, i):
        cur_range = int(i / self.index_range)
        range_index = int(i % self.index_range)
        color_index = int(range_index / self.gradient_range)
        start = (color_index % self.scheme.count)
        the_end = ((color_index + 1) % self.scheme.count)
        if cur_range % 2 != 0:
            start = self.scheme.count - 1 - start
            the_end = self.scheme.count - 1 - the_end

        return remap_color(range_index % self.gradient_range, 0, self.gradient_range, self.scheme.colors[start],
                           self.scheme.colors[the_end])

    def step(self, times=1):
        for i in range(times):
            self.render()

    def render(self):
        current_time_in_ms = int(time.time() * 1000)
        offset = 0
        if self.speed > 0:
            offset = current_time_in_ms / self.speed
        old_color = self.smooth_color_over_range(self.strip.num_pixels() - 1 + offset)
        for i in range(self.strip.num_pixels()):
            current_color = self.smooth_color_over_range(i + offset)
            new_color = current_color
            if self.speed > 0:
                new_color = remap_color(current_time_in_ms % self.speed, 0, self.speed, old_color, current_color)
            self.strip.set_color_of(i, new_color)
            old_color = current_color

    def compute_gradient_range(self):
        return int(math.ceil(self.index_range / 2))

    def compute_index_range(self):
        return int(math.ceil(self.strip.num_pixels() / self.repetitions))