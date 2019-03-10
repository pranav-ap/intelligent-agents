from core import RandomAgent2D, Environment2D, Facing
from enum import Enum


class Action(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2
    CLEAN = 3


class RandomVacuumAgent2D(RandomAgent2D):
    def __init__(self, actions, location=(0, 0), facing=Facing.NONE):
        RandomAgent2D.__init__(self, actions, location, facing)


class TrivialEnvironment2D(Environment2D):
    def initialize_env(self):
        pass

    def display(self):
        pass

    def generate_percept(self, agent):
        pass

    def perform_action(self, agent, action):
        pass

    def run(self, steps=1000):
        pass


def main():
    actions = [Action.NONE, Action.LEFT, Action.RIGHT, Action.CLEAN]
    agent = RandomVacuumAgent2D(actions=actions)
    env = TrivialEnvironment2D()


if __name__ == '__main__':
    main()
