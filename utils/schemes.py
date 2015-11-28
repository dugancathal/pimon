import random

import colors


class Scheme:
    def __init__(self, count, colorset):
        self.count = count
        self.colors = colorset


def random_scheme():
    name = random.choice(["christmas", "rgb", "hanukkah", "rainbow", "fire", "kwanzaa"])
    return get_scheme(name)


def get_scheme(name):
    return globals()[name]


christmas = Scheme(2, [
    colors.red,
    colors.green
])

rgb = Scheme(3, [
    colors.red,
    colors.green,
    colors.blue
])

hanukkah = Scheme(2, [
    colors.blue, colors.white
])

rainbow = Scheme(8, [
    colors.red,
    colors.orange,
    colors.yellow,
    colors.green,
    colors.blue,
    colors.indigo,
    colors.purple,
    colors.white
])

fire = Scheme(3, [
    colors.red,
    colors.lightyellow,
    colors.orange
])

kwanzaa = Scheme(3, [
    colors.red,
    colors.black,
    colors.green
])
