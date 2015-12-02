import argparse

from builds.multi_circle_build_fetcher import MultiCircleBuildFetcher
from neopixels import random_filler_on
from neopixels.multi_swipe import MultiSwipe
from neopixels.pixel_strip import PixelStrip
from utils import colors

parser = argparse.ArgumentParser(description='Monitor your build!')
parser.add_argument('--projects', action='store', nargs='+', type=str, required=True,
                    help='the project names/urls/whatever your build script needs')
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


def convert_to_colors(build_statuses, ordered_by=[]):
    return map(lambda x: build_statuses[x].to_color(), ordered_by)


if __name__ == "__main__":
    strip = PixelStrip()
    fetcher = MultiCircleBuildFetcher(args.projects, args.token)
    fetcher.kickoff()

    while True:
        build_colors = convert_to_colors(fetcher.builds(), ordered_by=args.projects)
        MultiSwipe(strip, build_colors).step(times=3)
        fetcher.kickoff()

        random_filler_on(strip).step(times=args.poll_frequency)
        strip.color_wipe(colors.black, reverse_wipe=True)
