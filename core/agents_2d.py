from core.agent_structures import RandomAgent, SimpleReflexAgent
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
