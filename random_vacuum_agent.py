from core import RandomAgent2D, Environment2D, Facing, Dirt
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
    def _initialize_env(self):
        self.add_thing(Dirt(), (0, 0))

    def _perform_action(self, agent, action):
        if action == Action.LEFT:
            agent.location = loc_A
        elif action == Action.RIGHT:
            agent.location = loc_B
        elif action == Action.CLEAN:
            for thing in self.things:
                if type(thing) == Dirt and thing.location == agent.location:
                    self.delete_thing(thing)

    def step(self):
        while not self.is_all_clean():
            agents = self.get_all_agents()
            for agent in agents:
                percept = self._get_things_at(agent.lcation)
                action = agent.decide_action(percept)
                self._perform_action(agent, action)

    def is_all_clean(self):
        if all(type(thing) != Dirt for thing in self.things):
            return True
        return False


def main():
    actions = [Action.NONE, Action.LEFT, Action.RIGHT, Action.CLEAN]
    agent = RandomVacuumAgent2D(actions=actions)

    env = TrivialEnvironment2D()
    env.add_thing(agent, (0, 1))
    env.step()


if __name__ == '__main__':
    main()
