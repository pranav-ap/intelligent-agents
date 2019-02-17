from thing import Thing
from utils import Facing

import networkx as nx


class Environment:
    def __init__(self):
        self.things = []
        self.env = []

    def initialize_env(self):
        raise NotImplementedError

    def generate_percept(self, agent):
        raise NotImplementedError

    def step(self):
        raise NotImplementedError

    def run(self, steps=1000):
        for step in range(steps):
            self.step()

    def get_neighbor_locations(self, location, radius=1):
        raise NotImplementedError

    def get_things_at(self, location, kind=Thing):
        raise NotImplementedError

    def get_things_near(self, location, radius=1, kind=Thing):
        raise NotImplementedError

    def add_thing(self, thing):
        if thing in self.things:
            print("Can't add the same thing twice")
        else:
            self.things.append(thing)

    def delete_thing(self, thing):
        try:
            self.things.remove(thing)
        except ValueError as e:
            print(e)


class Environment2D(Environment):
    def __init__(self, width=10, height=10):
        super().__init__()
        self.width = width
        self.height = height
        self.env = nx.grid_2d_graph(height, width)

    def initialize_env(self):
        raise NotImplementedError

    def generate_percept(self, agent):
        raise NotImplementedError

    def step(self):
        raise NotImplementedError

    def get_neighbor_locations(self, location: tuple, radius: int = 1):
        return list(self.env.neighbors(location))

    def get_things_at(self, location: tuple, kind=Thing):
        return [thing for thing in self.things if thing.location == location and isinstance(thing, kind)]

    def get_things_near(self, location: tuple, radius=1, kind=Thing):
        return [(loc, thing)
                for loc in self.get_neighbor_locations(location, radius)
                for thing in self.get_things_at(location=loc, kind=kind)]


# Walkers for the environment


class Walker2D:
    def __init__(self, location: tuple, facing=Facing.NULL):
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
