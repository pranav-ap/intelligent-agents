from enum import Enum
import networkx as nx
import random


class FloorState(Enum):
    CLEAN = 0
    DIRTY = 1


class Action(Enum):
    NONE = 0
    MOVE = 1
    CLEAN = 2


class VaccumEnvironment:
    def __init__(self, height = 3, width = 3):
        self.width = width
        self.floor = nx.grid_2d_graph(height, width)
        # set random floor state values for all the nodes
        # tile = (location, data)
        for _, data in self.floor.nodes(data=True):
            data['status'] = random.choice(list(FloorState))

    def display_floor(self):
        i = 0
        print('\n--- Floor ---', end='')
        for node in self.floor.nodes(data=True):
            if i % self.width == 0:
                print ('\n')
            print(node, end='\t')
            i += 1

    def get_neighbor_locations(self, location):
        return [n for n in self.floor.neighbors(location)]

    def get_random_location(self):
        return random.choice(list(self.floor.nodes()))
    

class SimpleReflexVaccumAgent:
    def __init__(self, environment):
        self.environment = environment
        self.location = environment.get_random_location()
    
    def get_percept(self):
        return self.environment.floor.nodes[location]['status']
    
    def decide_action(self, percept):
        if percept == FloorState.DIRTY:
            return Action.CLEAN
        return Action.MOVE

    def move(self):
        neighbor_locations = self.environment.get_neighbor_locations(self.location)
        self.location = random.choice(neighbor_locations)
    
    def clean(self):
        self.environment.floor.nodes[self.location]['status'] = FloorState.CLEAN
        
    def perform_action(self, action):
        if action == Action.CLEAN:
            self.clean()
        elif action == Action.MOVE:
            self.move()

    def run(self, limit = 5):
        count = 0

        while count < limit:
            self.environment.display_floor()
            print ('\n--- Current location ---')
            print(self.location)

            percept = self.get_percept()
            action = self.decide_action(percept)

            print('--- Action ---')
            print(action)
            
            self.perform_action(action)

            count += 1

        
def main():
    env = VaccumEnvironment(height = 2, width = 2)
    agent = SimpleReflexVaccumAgent(environment = env)

    agent.run()


if __name__ == "__main__":
    main()
