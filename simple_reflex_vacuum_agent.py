from lib.agents_2d import SimpleReflexAgent2D
from lib.environments import Environment2D, Dirt


loc_A, loc_B = (0, 0), (0, 1)  # The two locations for the Vacuum world


# class Action(Enum):
#     NONE = 0
#     LEFT = 1
#     RIGHT = 2
#     CLEAN = 3
#
# class Facing(Enum):
#     U = 0
#     R = 1
#     D = 2
#     L = 3
#     NONE = 4

class VacuumEnvironment(Environment2D):
    def __init__(self, width=3, height=3):
        super().__init__(width=width, height=height)
        self.initialize_env()

    def initialize_env(self):
        self.add_thing(Dirt(), (0, 0))

    def display(self):
        i = 0
        print('--- Floor ---', end='')
        for node in self.env.nodes(data=True):
            if i % self.width == 0:
                print('\n')
            print(node, end='\t')
            i += 1

    def generate_percept(self, agent):
        return agent.location, self.get_things_at(agent.location)

    def perform_action(self, agent, action):
        if action == Action.LEFT:
            agent.location = loc_A
        elif action == Action.RIGHT:
            agent.location = loc_B
        elif action == Action.CLEAN:
            for thing in self.things:
                if type(thing) == Dirt and thing.location == agent.location:
                    self.delete_thing(thing)

    def run(self, steps=10):
        while not self.is_all_clean():
            agents = self.get_all_agents()
            for agent in agents:
                percept = self.generate_percept(agent)
                action = agent.action(percept)
                self.perform_action(agent, action)

    def is_all_clean(self):
        if all(type(thing) != Dirt for thing in self.things):
            return True
        return False


class SimpleReflexVacuumAgent(SimpleReflexAgent2D):
    def __init__(self, actions, rules, location=(0, 0), facing=Facing.NONE):
        SimpleReflexAgent2D.__init__(self, actions, rules, location, facing)


def main():
    actions = [Action.NONE, Action.CLEAN, Action.LEFT, Action.RIGHT]
    rules = [
        {'state': (loc_A, Floor.DIRTY), 'action': Action.CLEAN},
        {'state': (loc_A, Floor.CLEAN), 'action': Action.RIGHT},
        {'state': (loc_B, Floor.DIRTY), 'action': Action.CLEAN},
        {'state': (loc_B, Floor.CLEAN), 'action': Action.LEFT}
    ]

    agent = SimpleReflexVacuumAgent(actions, rules)

    env = VacuumEnvironment(width=2, height=1)
    env.add_thing(agent)
    env.run()


if __name__ == '__main__':
    main()
