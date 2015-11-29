import argparse
import time

from builds import circleci
from neopixels.gradient import Gradient
from neopixels.pixel_strip import PixelStrip
from neopixels.twinkle import Twinkle
from utils import schemes, colors

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
parser.add_argument('--poll-frequency', action='store', type=int, default=30,
                    help='number of seconds to wait between polls')
parser.add_argument('--num-builds', action='store', type=int, default=1,
                    help='number of builds to poll and show')

args = parser.parse_args()
if __name__ == "__main__":
    strip = PixelStrip()
    fetcher = circleci.BuildFetcher(args.project, args.token, args.num_builds)

    while True:
        for index, build in enumerate(fetcher.builds()):
            strip.color_wipe(build.to_color())
            strip.color_wipe(colors.black)

        if args.filler == 'gradient':
            g = Gradient(strip, schemes.get_scheme(args.gradient), 8, 250)
            for i in range(args.poll_frequency):
                g.step()
                time.sleep(0.1)
        elif args.filler == 'twinkle':
            t = Twinkle(strip)
            for i in range(args.poll_frequency):
                t.step()
                time.sleep(0.1)
