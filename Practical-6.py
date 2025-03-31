class RecursiveDescentParser:
    def __init__(self, input_string):
        self.input = input_string.strip()  # Input string to parse
        self.position = 0  # Current position in input string

    def match(self, expected_char):
        """Match a specific character in the input string."""
        if self.position < len(self.input) and self.input[self.position] == expected_char:
            self.position += 1
            return True
        return False

    def parse_S(self):
        """Parse according to the S rule in the grammar: S → ( L ) | a"""
        if self.match('('):
            if not self.parse_L():
                return False
            if not self.match(')'):
                return False
        elif self.match('a'):
            pass  # a is valid
        else:
            return False  # Invalid string if neither '(' nor 'a'
        return True

    def parse_L(self):
        """Parse according to the L rule in the grammar: L → S L'"""
        if not self.parse_S():
            return False
        return self.parse_L_prime()

    def parse_L_prime(self):
        """Parse according to the L' rule: L' → , S L' | ε"""
        if self.match(','):
            if not self.parse_S():
                return False
            return self.parse_L_prime()  # Recurse for further elements
        return True  # ε case: nothing after this is also valid

    def validate(self):
        """Validate the input string against the grammar."""
        is_valid = self.parse_S() and self.position == len(self.input)
        return "Valid string" if is_valid else "Invalid string"

# Sample Testcases
def run_testcases():
    test_cases = [
        "( a )",  # Valid string
        "a",  # Valid string
        "(a)",  # Valid string
        "(a,a)",  # Valid string
        "(a,(a,a),a)",  # Valid string
        "(a,a),(a,a)",  # Valid string
        "a)",  # Invalid string
        "(a a,a a, (a,a),a",  # Invalid string
    ]
    
    for test in test_cases:
        parser = RecursiveDescentParser(test)
        result = parser.validate()
        print(f"Input: {test} -> {result}")

# Run testcases
run_testcases()
