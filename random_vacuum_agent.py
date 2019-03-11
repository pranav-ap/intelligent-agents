from core import RandomAgent2D, Environment2D, Dirt, Direction, Agent
from enum import Enum


class Action(Enum):
    NONE = 0
    FRONT = 0
    RIGHT = 1
    BACK = 2
    LEFT = 3
    CLEAN = 3


class RandomVacuumAgent2D(RandomAgent2D):
    def __init__(self, actions, location=(0, 0)):
        RandomAgent2D.__init__(self, actions, location)


class TrivialEnvironment2D(Environment2D):
    def _initialize_env(self):
        self.add_thing(Dirt(), (0, 0))

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

    def run(self, steps=20):
        while not self._is_all_clean():
            for agent in self._get_all_things(kind=Agent):
                percept = self._get_things_at(agent.location)
                action = agent.decide_action(percept)
                self._perform_action(agent, action)

    def _is_all_clean(self):
        return all(not isinstance(thing, Dirt) for thing in self.things)


def main():
    actions = [Action.NONE, Action.LEFT, Action.RIGHT, Action.CLEAN, Action.FRONT, Action.BACK]
    agent = RandomVacuumAgent2D(actions=actions)

    env = TrivialEnvironment2D()
    env.add_thing(agent, (0, 1))
    env.run()


if __name__ == '__main__':
    main()
