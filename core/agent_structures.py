from core.things import Thing

import random


""""Base Agent"""


class Agent(Thing):
    def __init__(self, actions):
        self.actions = actions

    def action(self, percept):
        raise NotImplementedError

    def interpret_input(self, percept):
        return percept


""""Agent Structures"""


class RandomAgent(Agent):
    def __init__(self, actions):
        Agent.__init__(self, actions)

    def action(self, _=None):
        return random.choice(self.actions)
