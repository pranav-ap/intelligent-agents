from thing import Thing
from utils import rule_match

import random


""""Base Agent"""


class Agent(Thing):
    def __init__(self, actions, location):
        super().__init__(location)
        self.actions = actions

    def get_action(self, percept):
        raise NotImplementedError

    def interpret_input(self, percept):
        return percept


""""Agent Structures"""


class RandomAgent(Agent):
    def __init__(self, actions, location=None):
        super().__init__(actions, location)

    def get_action(self, _=None):
        return random.choice(self.actions)


class TableDrivenAgent(Agent):
    def __init__(self, actions, table, location=None):
        super().__init__(actions, location)
        self.percept_history = []
        self.table = table

    def get_action(self, percept):
        self.percept_history.append(percept)
        action = self.table.get(tuple(self.percept_history))
        return action


class SimpleReflexAgent(Agent):
    def __init__(self, actions, rules, location=None):
        super().__init__(actions, location)
        self.rules = rules

    def get_action(self, percept):
        state = self.interpret_input(percept)
        rule = rule_match(state, self.rules)
        action = rule.action
        return action


class ModelBasedReflexAgent(Agent):
    def __init__(self, actions, rules, location=None):
        super().__init__(actions, location)
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
