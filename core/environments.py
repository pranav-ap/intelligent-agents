from core.things import Thing
from core.agent_structures import Agent

import networkx as nx


class Environment:
    def __init__(self):
        self.things = []
        self.env = []

    def initialize_env(self):
        raise NotImplementedError

    def display(self):
        raise NotImplementedError

    def perform_action(self, agent, action):
        raise NotImplementedError

    def run(self, steps=1000):
        raise NotImplementedError

    def get_neighbor_locations(self, location):
        raise NotImplementedError

    def get_things_at(self, location, kind=Thing):
        raise NotImplementedError

    def get_things_around(self, location, kind=Thing):
        raise NotImplementedError

    def get_all_agents(self):
        raise NotImplementedError

    def add_thing(self, thing, location=None):
        if thing in self.things:
            print("Can't add the same thing twice")
        else:
            thing.location = location or thing.location or (0, 0)
            self.things.append(thing)

    def delete_thing(self, thing):
        try:
            self.things.remove(thing)
        except ValueError as e:
            print(e)


class Environment2D(Environment):
    def __init__(self, height=10, width=10):
        super().__init__()
        self.env = nx.grid_2d_graph(height, width)

    def initialize_env(self):
        raise NotImplementedError

    def display(self):
        raise NotImplementedError

    def generate_percept(self, agent):
        raise NotImplementedError

    def perform_action(self, agent, action):
        raise NotImplementedError

    def run(self, steps=1000):
        raise NotImplementedError

    def get_neighbor_locations(self, location: tuple):
        return list(self.env.neighbors(location))

    def get_things_at(self, location: tuple, kind=Thing):
        return [thing for thing in self.things if thing.location == location and isinstance(thing, kind)]

    def get_things_around(self, location: tuple, kind=Thing):
        return [(loc, thing)
                for loc in self.get_neighbor_locations(location)
                for thing in self.get_things_at(location=loc, kind=kind)]

    def get_all_agents(self):
        return [thing for thing in self.things if isinstance(thing, Agent)]
