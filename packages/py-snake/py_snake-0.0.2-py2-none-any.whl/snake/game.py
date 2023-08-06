# -*- coding: utf-8 -*-

from .input import DefaultKeyReader
from .engine import GameEngine
from .model import SnakeModel
from .view import Canvas, FOOD, BODY, VOID
from .common import Frame, SelfCollision, BoundaryCollision, GameOver


class Game(GameEngine):
    def __init__(self, config, key_reader_cls=DefaultKeyReader):
        super(Game, self).__init__(config.initial_speed)
        self.config = config
        self.frame = Frame(config.width, config.height)
        self.snake = SnakeModel(self.frame, config)

        def setup_canvas():
            canvas = Canvas(self.frame)
            canvas.register_overlay(lambda: self.snake.snake_body, BODY)
            canvas.register_overlay(lambda: self.snake.food_locations, FOOD)
            canvas.register_overlay(lambda: self.snake.empty_locations, VOID)
            canvas.register_score_hook(lambda: self.snake.score)
            canvas.register_speed_hook(lambda: self.speed)
            return canvas

        self.canvas = setup_canvas()
        self.key_reader = key_reader_cls()
        self.status_message = ""

    def run(self):
        try:
            self.start_game()
        except KeyboardInterrupt:
            self.stop_game()
        except Exception:
            raise

    def game_should_update_frame(self):
        last_key = self.key_reader.last_key()

        if self.elapsed_time < 1.0:
            self.canvas.render("Ready.")
            return

        if self.elapsed_time < 2.0:
            self.canvas.render("Set.")
            return

        if self.speed < self.config.max_speed:
            self.speed = self.initial_speed + (self.snake.score * self.config.speed_increase_factor)

        snake_should_grow = False
        if last_key is not None:
            if last_key == 'up':
                self.snake.face_up()
            elif last_key == 'down':
                self.snake.face_down()
            elif last_key == 'left':
                self.snake.face_left()
            elif last_key == 'right':
                self.snake.face_right()
            elif last_key == 'esc':
                self.stop_game()

        try:
            self.snake.step(snake_should_grow)
        except SelfCollision:
            self.status_message = "Collision with self!"
            self.stop_game()
        except BoundaryCollision:
            self.status_message = "Collision with wall!"
            self.stop_game()
        else:
            overlay_text = None
            if self.elapsed_time < 3.0:
                overlay_text = 'GO!'

            self.canvas.render(overlay_text)

    def game_should_capture_input(self):
        self.key_reader.capture()

    def game_did_end(self):
        self.canvas.render("Game Over.")
        if self.status_message:
            print(self.status_message)

        raise GameOver
