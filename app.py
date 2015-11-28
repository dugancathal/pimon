import sys
from builds import circleci
from neopixels.pixel_strip import PixelStrip

if __name__ == "__main__":
    strip = PixelStrip()
    circle_token = sys.argv[1]
    fetcher = circleci.BuildFetcher("TruHearing/echo", circle_token)

    for index, build in enumerate(fetcher.builds()):
        strip.color_wipe(build.to_color())
        strip.reset()

