from agents import Agent, TraceAgent

def TableDrivenAgentProgram(table):
    percepts = []

    def program(percept):
        percepts.append(percept)
        action = table.get(tuple(percepts))
        return action

    return program


def RandomAgentProgram(actions):
    return lambda percept: random.choice(actions)


def SimpleReflexAgentProgram(rules, interpret_input):
    def program(percept):
        state = interpret_input(percept)
        rule = rule_match(state, rules)
        action = rule.action
        return action

    return program


def ModelBasedReflexAgentProgram(rules, update_state, model):
    def program(percept):
        program.state = update_state(program.state, program.action, percept, model)
        rule = rule_match(program.state, rules)
        action = rule.action
        return action

    program.state = program.action = None

    return program

# Helpers
def rule_match(state, rules):
    for rule in rules:
        if rule.matches(state):
            return rule