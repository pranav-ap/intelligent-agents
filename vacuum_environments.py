from core import Environment2D, Dirt, Direction, Agent
from utils import Action
from random import choice


class VacuumEnvironment2D(Environment2D):
    def __init__(self, height=3, width=3):
        Environment2D.__init__(self, height=height, width=width)

    def _perform_action(self, agent, action):
        if action == Action.LEFT:
            agent.move(Direction.LEFT, self.height, self.width)
        elif action == Action.RIGHT:
            agent.move(Direction.RIGHT, self.height, self.width)
        elif action == Action.FRONT:
            agent.move(Direction.FRONT, self.height, self.width)
        elif action == Action.BACK:
            agent.move(Direction.BACK, self.height, self.width)
        elif action == Action.CLEAN:
            for thing in self.things:
                if isinstance(thing, Dirt) and thing.location == agent.location:
                    self.delete_thing(thing)

    def _is_all_clean(self):
        return all(not isinstance(thing, Dirt) for thing in self.things)

    def run(self, max_steps=20):
        raise NotImplementedError


class TrivialVacuumEnvironment2D(VacuumEnvironment2D):
    def __init__(self, height=3, width=3):
        VacuumEnvironment2D.__init__(self, height=height, width=width)

    def run(self, max_steps=20):
        step = 0
        while not self._is_all_clean() and step <= max_steps:
            self.display()
            for agent in self._get_all_things(kind=Agent):
                percept = self._get_things_at(agent.location)
                action = agent.decide_action(percept)
                self._perform_action(agent, action)
                print('{} performs {}'.format(agent, action))

            step += 1

        self.display()


class PartiallyObservableTrivialVacuumEnvironment2D(VacuumEnvironment2D):
    def __init__(self, height=3, width=3):
        VacuumEnvironment2D.__init__(self, height=height, width=width)

    def run(self, max_steps=20):
        step = 0
        while not self._is_all_clean() and step <= max_steps:
            self.display()
            for agent in self._get_all_things(kind=Agent):
                percept = choice([self._get_things_at(agent.location), []])
                action = agent.decide_action(percept)
                self._perform_action(agent, action)
                print('{} performs {}'.format(agent, action))

            step += 1

        self.display()
