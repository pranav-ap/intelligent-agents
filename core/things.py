class Thing:
    pass


class Dirt(Thing):
    def __init__(self, location=(0, 0)):
        self.location = location


class Wall(Thing):
    def __init__(self, location=(0, 0)):
        self.location = location
