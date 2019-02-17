from thing import Thing
from utils import rule_match, AgentStructure
from environments import Walker2D

import random


""""Base Agent"""


class Agent(Thing):
    def __init__(self, actions):
        self.actions = actions

    def get_action(self, percept):
        raise NotImplementedError

    def interpret_input(self, percept):
        return percept


""""Agent Structures"""


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


# Agents for 2D Environments


class RandomAgent2D(RandomAgent, Walker2D):
    pass


class TableDrivenAgent2D(RandomAgent, Walker2D):
    pass


class SimpleReflexAgent2D(RandomAgent, Walker2D):
    pass


class ModelBasedReflexAgent2D(RandomAgent, Walker2D):
    def transition_model(self):
        raise NotImplementedError

    def update_state(self, percept, action):
        raise NotImplementedError
