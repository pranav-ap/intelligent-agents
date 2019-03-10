from core.agent_structures import RandomAgent
from core.walkers import Walker2D, Facing


class RandomAgent2D(RandomAgent, Walker2D):
    def __init__(self, actions, location=(0, 0), facing=Facing.NONE):
        RandomAgent.__init__(self, actions)
        Walker2D.__init__(self, location, facing)
