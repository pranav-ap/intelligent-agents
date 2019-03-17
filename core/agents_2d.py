from core.agent_structures import RandomAgent, SimpleReflexAgent, ModelBasedReflexAgent
from core.walkers import Walker2D


class RandomAgent2D(RandomAgent, Walker2D):
    def __init__(self, actions, location=(0, 0)):
        RandomAgent.__init__(self, actions)
        Walker2D.__init__(self, location)


class SimpleReflexAgent2D(SimpleReflexAgent, Walker2D):
    def __init__(self, actions, location=(0, 0)):
        SimpleReflexAgent.__init__(self, actions)
        Walker2D.__init__(self, location)

    def decide_action(self, percept):
        raise NotImplementedError


class ModelBasedReflexAgent2D(ModelBasedReflexAgent, Walker2D):
    def __init__(self, actions, location=(0, 0)):
        ModelBasedReflexAgent.__init__(self, actions)
        Walker2D.__init__(self, location)
        self.env = None

    def initialize_internal_env(self, env):
        self.env = env

    def decide_action(self, percept):
        raise NotImplementedError

    def _update_state(self, percept):
        raise NotImplementedError
