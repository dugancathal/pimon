import argparse
import time

from builds import circleci
from neopixels.gradient import Gradient
from neopixels.pixel_strip import PixelStrip

parser = argparse.ArgumentParser(description='Monitor your build!')
parser.add_argument('--project', action='store', required=True,
                   help='the project name/url/whatever your build script needs')
parser.add_argument('--token', action='store', required=True,
                   help='the password/secret/what-have-you for logging into your build system')
parser.add_argument('--filler', action='store', default='cycle',
                    choices=['cycle', 'multitwinkle', 'twinkle', 'gradient'],
                    help='what to do when not showing you your build state')
parser.add_argument('--gradient', action='store', default='hanukkah',
                    help='the color scheme to show for the gradient filler')
parser.add_argument('--poll-frequency', action='store', default='30',
                    help='number of seconds to wait between polls')

args = parser.parse_args()
if __name__ == "__main__":
    strip = PixelStrip()
    fetcher = circleci.BuildFetcher(args.project, args.token)

    while True:
        for index, build in enumerate(fetcher.builds()):
            strip.color_wipe(build.to_color())
            strip.reset()

        Gradient(strip, args.gradient, 8, 250)

        time.sleep(args.poll_frequency)
