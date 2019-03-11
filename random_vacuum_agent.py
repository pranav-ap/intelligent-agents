from core import RandomAgent2D, Dirt
from vacuum_environments import TrivialVacuumEnvironment2D
from utils import Action


class RandomVacuumAgent2D(RandomAgent2D):
    def __init__(self, actions, location=(0, 0)):
        RandomAgent2D.__init__(self, actions, location)

    def __repr__(self):
        return 'RandomVacuumAgent2D'


def main():
    actions = [Action.LEFT, Action.RIGHT, Action.CLEAN]
    agent = RandomVacuumAgent2D(actions=actions)

    env = TrivialVacuumEnvironment2D(height=1, width=2)
    env.add_thing(agent, (0, 1))
    env.add_thing(Dirt(), (0, 0))
    env.run()


if __name__ == '__main__':
    main()
