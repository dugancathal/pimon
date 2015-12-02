import time
from neopixels.pixel_strip import PixelStrip
from neopixels.multi_swipe import MultiSwipe
from utils import schemes, colors

if __name__ == "__main__":
    strip = PixelStrip()
    swipe = MultiSwipe(strip, [colors.green, colors.yellow, colors.red, colors.blue])

    while True:
        swipe.step()
        print "Sleeping..."
        time.sleep(1)
