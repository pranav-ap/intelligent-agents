from core import ModelBasedReflexAgent2D, Dirt
from vacuum_environments import (
    TrivialVacuumEnvironment2D,
    PartiallyObservableTrivialVacuumEnvironment2D)
from utils import Action

from random import choice


class ModelBasedReflexVacuumAgent2D(ModelBasedReflexAgent2D):
    def __init__(self, actions, location=(0, 0)):
        ModelBasedReflexAgent2D.__init__(self, actions, location)

    def decide_action(self, percept):
        self._update_state(percept)

        if any(isinstance(thing, Dirt) for thing in self.env._get_things_at(self.location)):
            return Action.CLEAN
        elif self.location == (0, 0):
            return Action.RIGHT
        elif self.location == (0, 1):
            return Action.LEFT
        else:
            return choice([Action.LEFT, Action.RIGHT])

    def _update_state(self, percept):
        things = self.env._get_all_things()
        filter(lambda thing: thing.location != self.location, things)

        for thing in percept:
            if thing not in self.env.things:
                self.env.add_thing(thing, thing.location)

    def __repr__(self):
        return 'ModelBasedReflexVacuumAgent2D'


def main():
    actions = [Action.LEFT, Action.RIGHT, Action.CLEAN]
    agent = ModelBasedReflexVacuumAgent2D(actions=actions)
    internal_env = TrivialVacuumEnvironment2D(height=1, width=2)
    agent.initialize_internal_env(internal_env)

    env = PartiallyObservableTrivialVacuumEnvironment2D(height=1, width=2)
    env.add_thing(agent, (0, 1))
    env.add_thing(Dirt(), (0, 0))
    env.run()


if __name__ == '__main__':
    main()
