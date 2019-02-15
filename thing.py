class Thing:
    def __repr__(self):
        return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))

    def show_state(self):
        raise NotImplementedError
