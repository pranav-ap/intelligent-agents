from core import ModelBasedReflexAgent2D, Dirt
from vacuum_environments import TrivialVacuumEnvironment2D
from utils import Action

from random import choice


class ModelBasedReflexVacuumAgent2D(ModelBasedReflexAgent2D):
    def __init__(self, actions, location=(0, 0)):
        ModelBasedReflexAgent2D.__init__(self, actions, location)

    def decide_action(self, percept):
        if any(isinstance(thing, Dirt) for thing in percept):
            return Action.CLEAN
        elif self.location == (0, 0):
            return Action.RIGHT
        elif self.location == (0, 1):
            return Action.LEFT
        else:
            return choice([Action.LEFT, Action.RIGHT])

    def _update_state(self, percept, action):
        pass

    def __repr__(self):
        return 'ModelBasedReflexVacuumAgent2D'


def main():
    actions = [Action.LEFT, Action.RIGHT, Action.CLEAN]
    agent = ModelBasedReflexVacuumAgent2D(actions=actions)
    internal_env = TrivialVacuumEnvironment2D(height=1, width=2)
    agent.initialize_internal_env(internal_env)

    env = TrivialVacuumEnvironment2D(height=1, width=2)
    env.add_thing(agent, (0, 1))
    env.add_thing(Dirt(), (0, 0))
    env.run()


if __name__ == '__main__':
    main()
