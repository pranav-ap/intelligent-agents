from enum import Enum


class AgentStructure(Enum):
    RandomAgent = 0
    TableDrivenAgent = 1
    SimpleReflexAgent = 2
    ModelBasedReflexAgent = 3
    GoalBasedAgent = 4
    UtilityBasedAgent = 5


class Floor(Enum):
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
    NONE = 4


def rule_match(state, rules):
    for rule in rules:
        if rule.matches(state):
            return rule
    return {'state': None, 'action': Action.NONE}

