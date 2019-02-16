from agents import RandomAgent

loc_A, loc_B = (0, 0), (1, 0)  # The two locations for the Vacuum world
agent_loc = 'agent_loc'


class RandomVacuumAgent(RandomAgent):
    def __init__(self, actions):
        RandomAgent.__init__(self, actions)


def TableDrivenVacuumAgent():
    table = {((loc_A, 'Clean'),): 'Right',
             ((loc_A, 'Dirty'),): 'Suck',
             ((loc_B, 'Clean'),): 'Left',
             ((loc_B, 'Dirty'),): 'Suck',
             ((loc_A, 'Dirty'), (loc_A, 'Clean')): 'Right',
             ((loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
             ((loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck',
             ((loc_B, 'Dirty'), (loc_B, 'Clean')): 'Left',
             ((loc_A, 'Dirty'), (loc_A, 'Clean'), (loc_B, 'Dirty')): 'Suck',
             ((loc_B, 'Dirty'), (loc_B, 'Clean'), (loc_A, 'Dirty')): 'Suck'
             }

    return Agent(TableDrivenAgentProgram(table))


def SimpleReflexVacuumAgent():
    rules = [
        {'state': (loc_A, 'Dirty'), 'action': 'Suck'},
        {'state': (loc_B, 'Dirty'), 'action': 'Suck'},
        {'state': (loc_A, 'Clean'), 'action': 'Right'},
        {'state': (loc_B, 'Clean'), 'action': 'Left'}
    ]

    return Agent(SimpleReflexAgentProgram(rules, lambda percept: percept))


def ModelBasedReflexVacuumAgent():
    state = {loc_A: None, loc_B: None, agent_loc: loc_A}

    rules = [
        {'state': ((loc_A, 'Dirty'), (loc_B, 'Dirty'), (agent_loc, loc_A)), 'action': 'Suck'},
        {'state': ((loc_A, 'Clean'), (loc_B, 'Dirty'), (agent_loc, loc_A)), 'action': 'Right'},
        {'state': ((loc_A, 'Dirty'), (loc_B, 'Clean'), (agent_loc, loc_A)), 'action': 'Suck'},
        {'state': ((loc_A, 'Clean'), (loc_B, 'Clean'), (agent_loc, loc_A)), 'action': 'NoOp'},
        {'state': ((loc_A, 'Dirty'), (loc_B, 'Dirty'), (agent_loc, loc_B)), 'action': 'Suck'},
        {'state': ((loc_A, 'Clean'), (loc_B, 'Dirty'), (agent_loc, loc_B)), 'action': 'Suck'},
        {'state': ((loc_A, 'Dirty'), (loc_B, 'Clean'), (agent_loc, loc_B)), 'action': 'Left'},
        {'state': ((loc_A, 'Clean'), (loc_B, 'Clean'), (agent_loc, loc_B)), 'action': 'NoOp'}
    ]

    transition_model = [
        {'prev': ((loc_A, 'Dirty'), (loc_B, 'Dirty'), (agent_loc, loc_A)), 'action': 'Suck', 'next': ((loc_A, 'Clean'), (loc_B, 'Dirty'), (agent_loc, loc_A))},
        {'prev': ((loc_A, 'Clean'), (loc_B, 'Dirty'), (agent_loc, loc_A)), 'action': 'Right', 'next': ((loc_A, 'Clean'), (loc_B, 'Dirty'), (agent_loc, loc_B))},
        {'prev': ((loc_A, 'Dirty'), (loc_B, 'Clean'), (agent_loc, loc_A)), 'action': 'Suck', 'next': ((loc_A, 'Clean'), (loc_B, 'Clean'), (agent_loc, loc_A))},
        {'prev': ((loc_A, 'Clean'), (loc_B, 'Clean'), (agent_loc, loc_A)), 'action': 'NoOp', 'next': ((loc_A, 'Clean'), (loc_B, 'Clean'), (agent_loc, loc_A))},
        {'prev': ((loc_A, 'Dirty'), (loc_B, 'Dirty'), (agent_loc, loc_B)), 'action': 'Suck', 'next': ((loc_A, 'Dirty'), (loc_B, 'Clean'), (agent_loc, loc_B))},
        {'prev': ((loc_A, 'Clean'), (loc_B, 'Dirty'), (agent_loc, loc_B)), 'action': 'Suck', 'next': ((loc_A, 'Clean'), (loc_B, 'Clean'), (agent_loc, loc_B))},
        {'prev': ((loc_A, 'Dirty'), (loc_B, 'Clean'), (agent_loc, loc_B)), 'action': 'Left', 'next': ((loc_A, 'Dirty'), (loc_B, 'Clean'), (agent_loc, loc_A))},
        {'prev': ((loc_A, 'Clean'), (loc_B, 'Clean'), (agent_loc, loc_B)), 'action': 'NoOp', 'next': ((loc_A, 'Clean'), (loc_B, 'Clean'), (agent_loc, loc_B))}
    ]

    def update_model(percept):
        location, status = percept
        state[agent_loc] = location
        state[location] = status

    return Agent(ModelBasedReflexAgentProgram(state, rules, update_model, transition_model))
