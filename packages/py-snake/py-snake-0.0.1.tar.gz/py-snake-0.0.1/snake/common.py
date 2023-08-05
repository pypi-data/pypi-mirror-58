from collections import namedtuple


class Point(namedtuple('Point', ['x', 'y'])):
    def __eq__(self, other): return self.x == other.x and self.y == other.y
    def __add__(self, other): return Point(self.x + other.x, self.y + other.y)
    def __hash__(self): return hash(str(self))


class Frame:
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.surface_points = set(Point(x, y) for x in self.xrange for y in self.yrange)

    @property
    def origin_point(self):
        return Point(self.x, self.y)

    @property
    def center_point(self):
        return Point(int(self.width / 2), int(self.height / 2))

    @property
    def xrange(self):
        return range(self.origin_point.x, self.origin_point.x + self.width)

    @property
    def yrange(self):
        return range(self.origin_point.y, self.origin_point.y + self.height)

    def __contains__(self, point):
        return point in self.surface_points


class DirectionOffset:
    UP = Point(0, 1)
    DOWN = Point(0, -1)
    LEFT = Point(-1, 0)
    RIGHT = Point(1, 0)


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = []

    def push(self, item):
        if item not in self.cache:
            self.cache.insert(0, item)
            while len(self.cache) > self.max_size:
                self.cache.pop()

    def __contains__(self, item):
        return item in self.cache

    def __len__(self):
        return len(self.cache)


def format_seconds(seconds, fmt_str='{m}:{s:02d}'):
    m = int(seconds / 60)
    s = int(seconds - m * 60)
    return fmt_str.format(m=m, s=s)


class GameOver(Exception):
    pass


class SelfCollision(GameOver):
    pass


class BoundaryCollision(GameOver):
    pass
