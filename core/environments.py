from core.things import Thing
import networkx as nx


class Environment:
    def __init__(self):
        self.things = []
        self.env = []

    def _initialize_env(self):
        raise NotImplementedError

    def display(self):
        raise NotImplementedError

    def _perform_action(self, agent, action):
        raise NotImplementedError

    def _get_things_at(self, location: tuple, kind=Thing):
        return [thing for thing in self.things if thing.location == location and isinstance(thing, kind)]

    def _get_all_things(self, kind=Thing):
        return [thing for thing in self.things if isinstance(thing, kind)]

    def step(self):
        """
        For each agent in the environment
            provide a percept
            get action decision
            perform the action
        """
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
    def __init__(self, height=3, width=3):
        super().__init__()
        self.height = height
        self.width = width
        self.env = nx.grid_2d_graph(height, width)

    def _initialize_env(self):
        raise NotImplementedError

    def display(self):
        i = 0
        for node in self.env.nodes(data=True):
            if i % self.width == 0:
                print('\n')
            print(node, end='\t')
            i += 1

    def _perform_action(self, agent, action):
        raise NotImplementedError

    def step(self):
        raise NotImplementedError
