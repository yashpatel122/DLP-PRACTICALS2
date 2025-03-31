class CFG:
    def __init__(self):
        self.grammar = {
            "S": [["A", "B", "C"], ["D"]],
            "A": [["a"], ["ε"]],
            "B": [["b"], ["ε"]],
            "C": [["(", "S", ")"], ["c"]],
            "D": [["A", "C"]],
        }
        self.first = {non_terminal: set() for non_terminal in self.grammar}
        self.follow = {non_terminal: set() for non_terminal in self.grammar}
        self.follow["S"].add("$")  # The start symbol's follow set contains the end of input symbol.

    def compute_first(self):
        changed = True
        while changed:
            changed = False
            for non_terminal, productions in self.grammar.items():
                for production in productions:
                    first_before = self.first[non_terminal].copy()
                    # Process each symbol in the production
                    for symbol in production:
                        if symbol in self.grammar:  # Non-terminal
                            self.first[non_terminal].update(self.first[symbol] - {"ε"})
                        else:  # Terminal
                            self.first[non_terminal].add(symbol)
                            break
                    # If we get ε, process further symbols
                    if "ε" in self.first[symbol]:
                        self.first[non_terminal].add("ε")
                    if self.first[non_terminal] != first_before:
                        changed = True

    def compute_follow(self):
        changed = True
        while changed:
            changed = False
            for non_terminal, productions in self.grammar.items():
                for production in productions:
                    for i in range(len(production)):
                        if production[i] in self.grammar:  # If it's a non-terminal
                            follow_before = self.follow[production[i]].copy()
                            # Check if it's followed by other symbols
                            if i == len(production) - 1:  # If it's at the end of the production
                                self.follow[production[i]].update(self.follow[non_terminal])
                            else:
                                next_symbol = production[i + 1]
                                if next_symbol in self.grammar:  # If next symbol is a non-terminal
                                    self.follow[production[i]].update(self.first[next_symbol] - {"ε"})
                                else:  # If next symbol is a terminal
                                    self.follow[production[i]].add(next_symbol)
                            if self.follow[production[i]] != follow_before:
                                changed = True

    def print_sets(self):
        print("First Sets:")
        for non_terminal, first_set in self.first.items():
            print(f"First({non_terminal}) = {first_set}")

        print("\nFollow Sets:")
        for non_terminal, follow_set in self.follow.items():
            print(f"Follow({non_terminal}) = {follow_set}")

# Main code to compute First and Follow
cfg = CFG()
cfg.compute_first()
cfg.compute_follow()
cfg.print_sets()
