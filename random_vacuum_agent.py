from core import RandomAgent2D, Environment2D
from enum import Enum


class Action(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    CLEAN = 3


def main():
    actions = [Action.NONE, Action.LEFT, Action.RIGHT, Action.CLEAN]
    agent = RandomAgent2D(actions=actions)
    env = Environment2D()


if __name__ == '__main__':
    main()
