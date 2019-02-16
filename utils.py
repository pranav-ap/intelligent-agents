from enum import Enum
import networkx as nx
import random


class FloorState(Enum):
    CLEAN = 0
    DIRTY = 1


class Action(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    CLEAN = 3


class Facing(Enum):
    U = 0
    R = 1
    D = 2
    L = 3
    NULL = 4


def rule_match(state, rules):
    for rule in rules:
        if rule.matches(state):
            return rule


class VacuumEnvironment:
    def __init__(self, height=3, width=3):
        self.height = height
        self.width = width
        self.floor = nx.grid_2d_graph(height, width)
        # set random floor state values for all the nodes
        # tile = (location, data)
        for _, data in self.floor.nodes(data=True):
            data['status'] = random.choice(list(FloorState))

    def display_floor(self):
        i = 0
        print('--- Floor ---', end='')
        for node in self.floor.nodes(data=True):
            if i % self.width == 0:
                print('\n')
            print(node, end='\t')
            i += 1

    def get_neighbor_locations(self, location):
        return list(self.floor.neighbors(location))

    def get_random_location(self):
        return random.choice(list(self.floor.nodes()))

    def is_all_clean(self):
        for _, data in self.floor.nodes(data=True):
            if data['status'] == FloorState.DIRTY:
                return False
        return True

    def get_number_of_dirty_tiles(self):
        count = 0
        for _, data in self.floor.nodes(data=True):
            if data['status'] == FloorState.DIRTY:
                count += 1
        return count
