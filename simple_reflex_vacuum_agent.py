from core import SimpleReflexAgent2D, Dirt
from vacuum_environments import TrivialVacuumEnvironment2D
from utils import Action

from random import choice


class SimpleReflexVacuumAgent2D(SimpleReflexAgent2D):
    def __init__(self, actions, location=(0, 0)):
        SimpleReflexAgent2D.__init__(self, actions, location)

    def decide_action(self, percept):
        if any(isinstance(thing, Dirt) for thing in percept):
            return Action.CLEAN
        elif self.location == (0, 0):
            return Action.RIGHT
        elif self.location == (0, 1):
            return Action.LEFT
        else:
            return choice([Action.LEFT, Action.RIGHT])

    def __repr__(self):
        return 'SimpleReflexVacuumAgent2D'


def main():
    actions = [Action.LEFT, Action.RIGHT, Action.CLEAN]
    agent = SimpleReflexVacuumAgent2D(actions=actions)

    env = TrivialVacuumEnvironment2D(height=1, width=2)
    env.add_thing(agent, (0, 1))
    env.add_thing(Dirt(), (0, 0))
    env.run()


if __name__ == '__main__':
    main()
