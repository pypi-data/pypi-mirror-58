from .common import DirectionOffset

__all__ = ['SnakeModelController']


class SnakeModelController:
    def __init__(self, model):
        self.snake = model

    def face_up(self):
        self.snake.direction.offset = DirectionOffset.UP

    def face_down(self):
        self.snake.direction.offset = DirectionOffset.DOWN

    def face_left(self):
        self.snake.direction.offset = DirectionOffset.LEFT

    def face_right(self):
        self.snake.direction.offset = DirectionOffset.RIGHT

    def step(self, should_grow=False):
        self.snake.step(should_grow)
