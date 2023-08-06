# -*- coding: utf-8 -*-

class GameConfig:
    # Frame dimensions
    width = 30
    height = 15

    # Start the game at this speed
    initial_speed = 3.0

    # For every point scored, increase game speed by this amount
    speed_increase_factor = 0.15

    # Maximum game speed.
    max_speed = 30

    # Enforce collision with frame boundaries.
    solid_walls = True

    # Amount of food initially displayed on screen.
    initial_food_count = 1

    # Max amount of food ever displayed at one time.
    max_food_count = 5

    # Increment the number of food items displayed in game
    # once every 'food_increase_interval' points scored.
    # (Set to 0 to never increment food display count).
    food_increase_interval = 10
