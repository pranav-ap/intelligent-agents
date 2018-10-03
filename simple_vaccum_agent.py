from utils import Action, FloorState, VacuumEnvironment
import random


class SimpleReflexVacuumAgent:
    def __init__(self, environment):
        self.environment = environment
        self.location = environment.get_random_location()

    def get_percept(self):
        return self.environment.floor.nodes[self.location]['status']

    def decide_action(self, percept):
        if percept == FloorState.DIRTY:
            return Action.CLEAN
        return Action.MOVE

    def move(self):
        neighbor_locations = self.environment.get_neighbor_locations(
            self.location)
        self.location = random.choice(neighbor_locations)

    def clean(self):
        self.environment.floor.nodes[self.location]['status'] = FloorState.CLEAN

    def perform_action(self, action):
        if action == Action.CLEAN:
            self.clean()
        elif action == Action.MOVE:
            self.move()

    def run(self, limit=10):
        count = 0

        print('Initial no of dirty tiles : ' +
              str(self.environment.get_number_of_dirty_tiles()))

        while count < limit:
            percept = self.get_percept()
            action = self.decide_action(percept)
            self.perform_action(action)

            count += 1

        print('Final no of dirty tiles : ' +
              str(self.environment.get_number_of_dirty_tiles()))


def main():
    env = VacuumEnvironment(height=5, width=5)
    agent = SimpleReflexVacuumAgent(environment=env)

    agent.run()


if __name__ == "__main__":
    main()
