from core.utils import Facing


""" Walkers for the environment """


class Walker2D:
    def __init__(self, location: tuple, facing=Facing.NONE):
        self.location = location
        self.facing = facing

    def turn(self, turn_direction):
        value = (self.facing.value + turn_direction.value) % 4
        self.facing = Facing(value)

    def move_forward(self):
        x, y = self.facing

        if self.facing == Facing.R:
            self.location = (x + 1, y)
        elif self.facing == Facing.L:
            self.location = (x - 1, y)
        elif self.facing == Facing.U:
            self.location = (x, y + 1)
        elif self.facing == Facing.D:
            self.location = (x, y - 1)
