from thing import Thing
from utils import Facing, rule_match

import random


""""Base Agent"""


class Agent(Thing):
    def __init__(self, actions):
        self.actions = actions

    def get_action(self, percept):
        raise NotImplementedError

    def interpret_input(self, percept):
        return percept


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


""""Agent Structures"""


def AgentFactory(agent_structure, dimensions):
    pass


class RandomAgent(Agent):
    def __init__(self, actions):
        super().__init__(actions)

    def get_action(self, _=None):
        return random.choice(self.actions)


class TableDrivenAgent(Agent):
    def __init__(self, actions, table):
        super().__init__(actions)
        self.percept_history = []
        self.table = table

    def get_action(self, percept):
        self.percept_history.append(percept)
        action = self.table.get(tuple(self.percept_history))
        return action


class SimpleReflexAgent(Agent):
    def __init__(self, actions, rules):
        super().__init__(actions)
        self.rules = rules

    def get_action(self, percept):
        state = self.interpret_input(percept)
        rule = rule_match(state, self.rules)
        action = rule.action
        return action


class ModelBasedReflexAgent(Agent):
    def __init__(self, actions, rules):
        super().__init__(actions)
        self.rules = rules
        self.state = None

    def get_action(self, percept):
        percept = self.interpret_input(percept)

        rule = rule_match(self.state, self.rules)
        action = rule.action

        self.state = self.update_state(percept, action)

        return action

    def transition_model(self):
        raise NotImplementedError

    def update_state(self, percept, action):
        raise NotImplementedError
