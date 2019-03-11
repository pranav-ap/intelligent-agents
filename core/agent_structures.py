from core.things import Thing

from random import choice


""""Base Agent"""


class Agent(Thing):
    def __init__(self, actions):
        self.actions = actions

    def decide_action(self, percept):
        raise NotImplementedError

    def interpret_input(self, percept):
        return percept


""""Agent Structures"""


class RandomAgent(Agent):
    def __init__(self, actions):
        Agent.__init__(self, actions)

    def decide_action(self, _):
        return choice(self.actions)


class SimpleReflexAgent(Agent):
    def __init__(self, actions):
        Agent.__init__(self, actions)

    def decide_action(self, percept):
        raise NotImplementedError
