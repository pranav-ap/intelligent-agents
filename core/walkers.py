from enum import Enum


class Direction(Enum):
    FRONT = 0
    RIGHT = 1
    BACK = 2
    LEFT = 3
    CURRENT = 4
    NONE = 5


"""
Walkers for the environment 
---------------------------
This class handles the location data and navigation actions for an agent.
"""


class Walker:
    def __init__(self, location: tuple):
        self.location = location

    def move(self, direction: Direction, env_height, env_width) -> None:
        raise NotImplementedError


class Walker2D(Walker):
    def __init__(self, location: tuple):
        Walker.__init__(self, location=location)

    def move(self, direction: Direction, env_height, env_width) -> None:
        x, y = self.location

        if direction == Direction.EAST and y + 1 < env_width:
            self.location = x, y + 1
        elif direction == Direction.WEST and y - 1 >= 0:
            self.location = x, y - 1
        elif direction == Direction.NORTH and x - 1 <= 0:
            self.location = x - 1, y
        elif direction == Direction.SOUTH and x + 1 > env_height:
            self.location = x + 1, y
