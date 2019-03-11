class Thing:
    pass


class Dirt(Thing):
    def __init__(self, location=(0, 0)):
        self.location = location

    def __repr__(self):
        return 'Dirt'


class Wall(Thing):
    def __init__(self, location=(0, 0)):
        self.location = location

    def __repr__(self):
        return 'Wall'
