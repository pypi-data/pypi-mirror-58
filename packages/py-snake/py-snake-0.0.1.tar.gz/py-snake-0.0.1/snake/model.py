from .common import Point, LRUCache, SelfCollision, BoundaryCollision, DirectionOffset

__all__ = ['SnakeModel']


class DirectionState:
    UP = DirectionOffset.UP
    DOWN = DirectionOffset.DOWN
    LEFT = DirectionOffset.LEFT
    RIGHT = DirectionOffset.RIGHT

    legal_transitions = {
        UP: (LEFT, RIGHT),
        DOWN: (LEFT, RIGHT),
        LEFT: (UP, DOWN),
        RIGHT: (UP, DOWN)
    }

    def __init__(self, model, initial_direction=UP):
        self.model = model
        self._offset = initial_direction

    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, proposed):
        if proposed not in self.legal_transitions[self.offset]:
            if len(self.model) > 1:
                # warnings.warn("Snake cannot move this direction.")
                return

        self._offset = proposed


class SnakeModel:
    def __init__(self, frame, config):
        self.frame = frame
        self.config = config
        self.snake_body = [frame.center_point + Point(0, -1 * int(frame.height / 4))]
        self.food_count = config.initial_food_count
        self.solid_walls = config.solid_walls
        self.direction = DirectionState(self)
        self.food_locations = []
        self.lru_food_locations = LRUCache(int((frame.width + frame.height) / 3))
        self.status_message = ''

    def face_up(self):
        self.direction.offset = DirectionOffset.UP

    def face_down(self):
        self.direction.offset = DirectionOffset.DOWN

    def face_left(self):
        self.direction.offset = DirectionOffset.LEFT

    def face_right(self):
        self.direction.offset = DirectionOffset.RIGHT

    def step(self, should_grow=False):
        new_location = self.head_location + self.direction.offset

        if new_location in self:
            raise SelfCollision

        if self.solid_walls and new_location not in self.frame:
            raise BoundaryCollision

        self.snake_body.insert(0, new_location)

        if new_location in self.food_locations:
            self.food_locations.remove(new_location)
            should_grow = True

        if not should_grow:
            self.snake_body.pop()

        if self.config.food_increase_interval > 0 and self.food_count < self.config.max_food_count:
            self.food_count = self.config.initial_food_count + int(self.score / self.config.food_increase_interval)

        while len(self.food_locations) < self.food_count and len(self.available_food_locations) > 0:
            location = self.available_food_locations.pop()
            self.food_locations.append(location)
            self.lru_food_locations.push(location)

    @property
    def head_location(self):
        return self.snake_body[0]

    @property
    def occupied_locations(self):
        return set(self.snake_body) | set(self.food_locations)

    @property
    def empty_locations(self):
        return self.frame.surface_points - self.occupied_locations

    @property
    def available_food_locations(self):
        return self.empty_locations - set(self.lru_food_locations.cache)

    @property
    def score(self):
        return len(self.snake_body) - 1

    def __contains__(self, point):
        return point in self.snake_body

    def __len__(self):
        return len(self.snake_body)
