class FiniteAutomaton:
    def __init__(self, states, input_symbols, transitions, initial_state, accept_states):
        self.states = states
        self.input_symbols = input_symbols
        self.transitions = transitions
        self.initial_state = initial_state
        self.accept_states = accept_states

    def validate_string(self, input_string):
        current_state = self.initial_state
        
        for symbol in input_string:
            if symbol not in self.input_symbols or current_state not in self.transitions:
                return "Invalid String"
            
            if symbol in self.transitions[current_state]:
                current_state = self.transitions[current_state][symbol]
            else:
                return "Invalid String"
        
        return "Valid String" if current_state in self.accept_states else "Invalid String"

def main():
    num_symbols = int(input("Number of input symbols: "))
    input_symbols = input("Input symbols: ").split()

    num_states = int(input("Enter number of states: "))
    states = set(range(1, num_states + 1))

    initial_state = int(input("Initial state: "))

    num_accept_states = int(input("Number of accepting states: "))
    accept_states = set(map(int, input("Accepting states: ").split()))

    transitions = {}
    print("Enter transition table:")
    for _ in range(num_states):
        state = int(input("State: "))
        transitions[state] = {}
        for symbol in input_symbols:
            next_state = int(input(f"{state} to {symbol} -> "))
            transitions[state][symbol] = next_state

    fa = FiniteAutomaton(states, input_symbols, transitions, initial_state, accept_states)

    input_string = input("Input string: ")
    print(fa.validate_string(input_string))

if __name__ == "__main__":
    main()
