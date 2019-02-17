from utils import Action, Floor, VacuumEnvironment
import random

# percept only shows current tile
# has a broken sensor and actuator
# 50% chance that percept is wrong - may incorrectly say tile is clean
# 50% chance that actuator will not clean/ puts dirt back into tile


class ModelBasedVacuumAgent:
    def __init__(self, external_env):
        self.external_env = external_env
        self.env = VacuumEnvironment(
            height=self.external_env.height, width=self.external_env.width)
        self.location = self.env.get_random_location()

    def get_percept(self):
        # get percepts from internal env
        percept = self.external_env.floor.nodes[self.location]['status']
        return random.choice([percept, Floor.CLEAN])

    def decide_action(self):
        # decide based on internal model
        if self.env.floor.nodes[self.location]['status'] == Floor.DIRTY:
            return Action.CLEAN
        return Action.MOVE

    def move(self):
        neighbor_locations = self.env.get_neighbor_locations(self.location)
        self.location = random.choice(neighbor_locations)

    def clean(self):
        self.env.floor.nodes[self.location]['status'] = Floor.CLEAN
        # randomly clean the external tile to simulate a broken vaccum cleaner
        self.external_env.floor.nodes[self.location]['status'] = random.choice(
            list(Floor))

    # perform action on both env
    def perform_action(self, action):
        if action == Action.CLEAN:
            self.clean()
        elif action == Action.MOVE:
            self.move()

    def update_internal_env(self, percept):
        self.env.floor.nodes[self.location]['status'] = percept

    def run(self, limit=5):
        count = 0

        print('Initial no of dirty tiles : ' +
              str(self.external_env.get_number_of_dirty_tiles()))

        while count < limit and not self.env.is_all_clean():
            percept = self.get_percept()
            self.update_internal_env(percept)
            action = self.decide_action()
            self.perform_action(action)

            count += 1

        print('Final no of dirty tiles : ' +
              str(self.external_env.get_number_of_dirty_tiles()))


def main():
    external_env = VacuumEnvironment(height=10, width=10)
    agent = ModelBasedVacuumAgent(external_env=external_env)

    agent.run()


if __name__ == "__main__":
    main()
