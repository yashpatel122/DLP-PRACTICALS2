class LL1Parser:
    def __init__(self):
        # Sample grammar
        self.grammar = {
            "S": [["A", "B", "C"], ["D"]],
            "A": [["a"], ["ε"]],
            "B": [["b"], ["ε"]],
            "C": [["(", "S", ")"], ["c"]],
            "D": [["A", "C"]],
        }
        self.first = {
            "S": {"a", "b", "(", "c"},
            "A": {"a", "ε"},
            "B": {"b", "ε"},
            "C": {"(", "c"},
            "D": {"a", "(", "c"}
        }
        self.follow = {
            "S": {")", "$"},
            "A": {"b", "(", "c"},
            "B": {"(", "c"},
            "C": {")", "$"},
            "D": {")", "$"}
        }
        self.parsing_table = {}
        self.build_parsing_table()

    def build_parsing_table(self):
        """
        Build the predictive parsing table for the given grammar.
        """
        for non_terminal, productions in self.grammar.items():
            self.parsing_table[non_terminal] = {}
            for production in productions:
                first_set = self.first[production[0]] if production[0] in self.first else {production[0]}
                if "ε" in first_set:
                    first_set.remove("ε")
                    follow_set = self.follow[non_terminal]
                    for terminal in first_set:
                        self.parsing_table[non_terminal][terminal] = production
                for terminal in first_set:
                    self.parsing_table[non_terminal][terminal] = production

    def check_ll1(self):
        """
        Check if the grammar is LL(1).
        """
        for non_terminal, terminals in self.parsing_table.items():
            for terminal, production in terminals.items():
                if terminal in self.parsing_table[non_terminal]:
                    return False
        return True

    def validate_string(self, input_string):
        """
        Validate an input string using the predictive parsing table.
        """
        stack = ["$", "S"]
        input_string = input_string + "$"
        idx = 0
        while stack:
            top = stack.pop()
            symbol = input_string[idx]
            if top == symbol:
                idx += 1
            elif top in self.grammar:
                production = self.parsing_table[top].get(symbol, None)
                if not production:
                    return "Invalid string"
                stack.extend(reversed(production))
            else:
                return "Invalid string"
        return "Valid string" if not stack else "Invalid string"

    def print_parsing_table(self):
        """
        Print the generated parsing table.
        """
        print("Parsing Table:")
        for non_terminal, table in self.parsing_table.items():
            print(f"{non_terminal}: {table}")


# Main code to execute the LL(1) parser
parser = LL1Parser()
parser.print_parsing_table()

if parser.check_ll1():
    print("\nGrammar is LL(1).")
    input_string = input("\nEnter a string to validate: ")
    result = parser.validate_string(input_string)
    print(result)
else:
    print("\nGrammar is not LL(1).")
