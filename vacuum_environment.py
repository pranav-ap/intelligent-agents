from environments import Environment2D
from utils import Floor

import random


class VacuumEnvironment(Environment2D):
    def __init__(self, width=3, height=3):
        super().__init__(width=width, height=height)
        self.initialize_env()

    def initialize_env(self):
        for _, data in self.env.nodes(data=True):
            data['status'] = random.choice([Floor.Clean, Floor.Dirty])

    def display(self):
        i = 0
        print('--- Floor ---', end='')
        for node in self.env.nodes(data=True):
            if i % self.width == 0:
                print('\n')
            print(node, end='\t')
            i += 1

    def generate_percept(self, agent):
        return self.get_things_at(agent.location)

    def run(self, steps=1000):
        while not self.is_all_clean():
            agents = self.get_all_agents()
            for agent in agents:
                percept = self.generate_percept(agent)
                agent.action(percept)

    def is_all_clean(self):
        for _, data in self.env.nodes(data=True):
            if data['status'] == Floor.DIRTY:
                return False
        return True
