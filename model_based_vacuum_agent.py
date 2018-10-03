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


class VacuumEnvironment:
    def __init__(self, height = 3, width = 3):
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
                print ('\n')
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

# percept only shows current tile
# has a broken sensor and actuator
# 50% chance that percept is wrong - may incorrectly say tile is clean
# 50% chance that actuator will not clean/ puts dirt back into tile
class ModelBasedVacuumAgent:
    def __init__(self, external_env):
        self.external_env = external_env
        self.env = VacuumEnvironment(height = self.external_env.height, width = self.external_env.width)
        self.location = self.env.get_random_location()
    
    def get_percept(self):
        # get percepts from internal env
        percept = self.external_env.floor.nodes[self.location]['status']
        return random.choice([percept, FloorState.CLEAN])
    
    def decide_action(self):
        # decide based on internal model
        if self.env.floor.nodes[self.location]['status'] == FloorState.DIRTY:
            return Action.CLEAN
        return Action.MOVE

    def move(self):
        neighbor_locations = self.env.get_neighbor_locations(self.location)
        self.location = random.choice(neighbor_locations)
    
    def clean(self):
        self.env.floor.nodes[self.location]['status'] = FloorState.CLEAN
        # randomly clean the external tile to simulate a broken vaccum cleaner
        self.external_env.floor.nodes[self.location]['status'] = random.choice(list(FloorState))
                
    # perform action on both env
    def perform_action(self, action):
        if action == Action.CLEAN:
            self.clean()
        elif action == Action.MOVE:
            self.move()
    
    def update_internal_env(self, percept):
        self.env.floor.nodes[self.location]['status'] = percept

    def run(self, limit = 5):
        count = 0

        print('\nInitial')
        self.external_env.display_floor()

        while count < limit and not self.env.is_all_clean():
            percept = self.get_percept()
            self.update_internal_env(percept)
            action = self.decide_action()
            self.perform_action(action)

            count += 1
        
        print ('\nFinal')
        print('count : ' + str(count))
        self.external_env.display_floor()        

        
def main():
    external_env = VacuumEnvironment(height = 2, width = 2)
    agent = ModelBasedVacuumAgent(external_env = external_env)

    agent.run()


if __name__ == "__main__":
    main()
