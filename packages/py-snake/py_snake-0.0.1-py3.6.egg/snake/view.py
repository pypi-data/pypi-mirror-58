# -*- coding: utf-8 -*-

import os
import functools

from .common import Point

NW, TOP, NE = '┌', '─', '┐'
LT, CTR, RT = '│', ' ', '│'
SW, BTM, SE = '└', '─', '┘'
BODY = '█'
FOOD = '*'


class Canvas:
    def __init__(self, frame, model, game):
        self.frame = frame
        self.model = model
        self.game = game
        self.grid = {}
        self.clear_console = functools.partial(os.system, 'cls' if os.name == 'nt' else 'clear')
        self.reset()

    def render(self, message=None):
        self.overlay(self.model.snake_body, BODY)
        self.overlay(self.model.food_locations, FOOD)
        self.overlay(self.model.empty_locations, CTR)
        if message:
            for i, char in enumerate(message):
                x_offset = -1 * int(len(message) / 2) + i
                y_offset = -1 * int(self.frame.height / 4)
                self.overlay([self.frame.center_point + Point(x_offset, 0)], char)
        self.print_to_console()

    def reset(self):
        self.grid = {point: CTR for point in self.frame.surface_points}

    def overlay(self, points, char):
        for point in points:
            self.grid[point] = char

    def print_to_console(self):
        self.clear_console()
        speed_text = 'Speed: {:.02f}'.format(self.game.speed)
        coverage_text = 'Cov: {:.0f}%'.format((len(self.model) / len(self.frame.surface_points) * 100))
        print('{} {}'.format(speed_text, coverage_text.rjust(self.frame.width - len(speed_text) + 1, CTR)))
        print(''.join([NW] + [TOP] * self.frame.width + [NE]))
        for y in self.frame.yrange:
            chars = [self.grid[Point(x, self.frame.height - y - 1)] for x in self.frame.xrange]
            print(''.join([LT] + chars + [RT]))
        print(''.join([SW] + [BTM] * self.frame.width + [SE]))
        print('Score: {}'.format(self.model.score))
