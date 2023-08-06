# -*- coding: utf-8 -*-

import os
import sys
import functools

from .common import Point

if sys.version_info.major == 2 and os.name == 'nt':
    NW, NN, NE = ' ', '-', ' '
    WW, XX, EE = '|', ' ', '|'
    SW, SS, SE = ' ', '-', ' '
    BODY, FOOD = '#', '*'

else:
    NW, NN, NE = '┌', '─', '┐'
    WW, XX, EE = '│', ' ', '│'
    SW, SS, SE = '└', '─', '┘'
    FOOD, BODY = '*', '█'

VOID = XX



class Canvas:
    def __init__(self, frame):
        self.frame = frame
        self.grid = {}
        self.overlays = []
        self.speed_hook = None
        self.score_hook = None
        self.clear_console = functools.partial(os.system, 'cls' if os.name == 'nt' else 'clear')
        self.reset()

    def register_overlay(self, points_array_getter, character):
        self.overlays.append((points_array_getter, character))

    def register_speed_hook(self, speed_hook):
        self.speed_hook = speed_hook

    def register_score_hook(self, score_hook):
        self.score_hook = score_hook

    def reset(self):
        self.grid = {point: XX for point in self.frame.surface_points}

    def render(self, message=None):
        for points_getter, character in self.overlays:
            self.overlay(points_getter(), character)
        if message:
            for i, char in enumerate(message):
                x_offset = -1 * int(len(message) / 2) + i
                y_offset = -1 * int(self.frame.height / 4)
                self.overlay([self.frame.center_point + Point(x_offset, 0)], char)
        self.print_to_console()

    def overlay(self, points, char):
        for point in points:
            self.grid[point] = char

    def print_to_console(self):
        self.clear_console()
        speed_text = 'Speed: {:.02f}'.format(self.speed)
        coverage_text = 'Cov: {:.0f}%'.format(self.coverage)
        print('{} {}'.format(speed_text, coverage_text.rjust(self.frame.width - len(speed_text) + 1, XX)))
        print(''.join([NW] + [NN] * self.frame.width + [NE]))
        for y in self.frame.yrange:
            chars = [self.grid[Point(x, self.frame.height - y - 1)] for x in self.frame.xrange]
            print(''.join([WW] + chars + [EE]))
        print(''.join([SW] + [SS] * self.frame.width + [SE]))
        print('Score: {}'.format(self.score))

    @property
    def speed(self):
        return self.speed_hook()

    @property
    def score(self):
        return self.score_hook()

    @property
    def coverage(self):
        return (1 + self.score) / len(self.frame.surface_points) * 100
