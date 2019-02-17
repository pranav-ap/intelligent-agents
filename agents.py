from thing import Thing
from utils import rule_match, Facing
from environments import Walker2D

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
        super().__init__(actions)

    def action(self, _=None):
        return random.choice(self.actions)


class TableDrivenAgent(Agent):
    def __init__(self, actions, table):
        super().__init__(actions)
        self.percept_history = []
        self.table = table

    def action(self, percept):
        self.percept_history.append(percept)
        action = self.table.get(tuple(self.percept_history))
        return action


class SimpleReflexAgent(Agent):
    def __init__(self, actions, rules):
        super().__init__(actions)
        self.rules = rules

    def action(self, percept):
        state = self.interpret_input(percept)
        rule = rule_match(state, self.rules)
        action = rule.action
        return action


class ModelBasedReflexAgent(Agent):
    def __init__(self, actions, rules):
        super().__init__(actions)
        self.rules = rules
        self.state = None

    def action(self, percept):
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
    def __init__(self, actions, location=(0, 0), facing=Facing.NONE):
        RandomAgent.__init__(self, actions)
        Walker2D.__init__(self, location, facing)


class TableDrivenAgent2D(TableDrivenAgent, Walker2D):
    def __init__(self, actions, table, location=(0, 0), facing=Facing.NONE):
        TableDrivenAgent.__init__(self, actions, table)
        Walker2D.__init__(self, location, facing)


class SimpleReflexAgent2D(SimpleReflexAgent, Walker2D):
    def __init__(self, actions, rules, location=(0, 0), facing=Facing.NONE):
        SimpleReflexAgent.__init__(self, actions, rules)
        Walker2D.__init__(self, location, facing)


class ModelBasedReflexAgent2D(ModelBasedReflexAgent, Walker2D):
    def __init__(self, actions, rules, location=(0, 0), facing=Facing.NONE):
        ModelBasedReflexAgent.__init__(self, actions, rules)
        Walker2D.__init__(self, location, facing)

    def transition_model(self):
        raise NotImplementedError

    def update_state(self, percept, action):
        raise NotImplementedError
