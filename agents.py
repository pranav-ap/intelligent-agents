from thing import Thing

class Agent(Thing):
    """An Agent is a subclass of Thing with one required slot,
    .program, which should hold a function that takes one argument, the
    percept, and returns an action."""
    def __init__(self, program=None):
        self.performance = 0

        if program is None or not isinstance(program, collections.Callable):
            raise ValueError("Can't find a valid program for {}.".format(self.__class__.__name__))

        self.program = program


def TraceAgent(agent):
    """Wrap the agent's program to print its input and output. This will let
    you see what the agent is doing in the environment."""
    old_program = agent.program

    def new_program(percept):
        action = old_program(percept)
        print('{} perceives {} and does {}'.format(agent, percept, action))
        return action

    agent.program = new_program

    return agent
