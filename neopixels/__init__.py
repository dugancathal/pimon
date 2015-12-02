from neopixels.gradient import Gradient
from neopixels.twinkle import Twinkle
from utils import schemes
from random import choice as random_one_of


def random_filler_on(strip):
    return random_one_of([
        Gradient(strip, schemes.random_scheme(), 8, 100)
    ])
