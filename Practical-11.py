import re

# Class to represent each quadruple
class Quadruple:
    def __init__(self, operator, operand1, operand2, result):
        self.operator = operator
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result

    def __str__(self):
        return f"({self.operator}, {self.operand1}, {self.operand2}, {self.result})"


class IntermediateCodeGenerator:
    def __init__(self):
        self.temp_count = 1  # To create unique temporary variable names
        self.quadruples = []  # To store the generated quadruples

    def generate_temp(self):
        temp = f"t{self.temp_count}"
        self.temp_count += 1
        return temp

    def parse_expression(self, expression):
        # Tokenize the expression
        tokens = re.findall(r'\d+\.\d+|\d+|[+*/^()-]', expression)

        # Create a stack for the operands and operators
        operand_stack = []
        operator_stack = []
        
        # Parse the expression
        for token in tokens:
            if token.isdigit():  # If the token is a digit, push it onto the operand stack
                operand_stack.append(token)
            elif token == '(':  # If the token is a left parenthesis, push it onto the operator stack
                operator_stack.append(token)
            elif token == ')':  # If the token is a right parenthesis, pop from the stacks until '('
                while operator_stack[-1] != '(':
                    self.process_operator(operand_stack, operator_stack.pop())
                operator_stack.pop()  # Remove '(' from stack
            else:  # If the token is an operator
                while (operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(token)):
                    self.process_operator(operand_stack, operator_stack.pop())
                operator_stack.append(token)

        # Process remaining operators in the stack
        while operator_stack:
            self.process_operator(operand_stack, operator_stack.pop())

        return self.quadruples

    def process_operator(self, operand_stack, operator):
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        result = self.generate_temp()
        self.quadruples.append(Quadruple(operator, operand1, operand2, result))
        operand_stack.append(result)

    def precedence(self, operator):
        precedence_dict = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return precedence_dict.get(operator, 0)


# Function to display the quadruples
def print_quadruples(quadruples):
    print("Operator\tOperand 1\tOperand 2\tResult")
    for q in quadruples:
        print(f"{q.operator}\t\t{q.operand1}\t\t{q.operand2}\t\t{q.result}")


# Driver code
if __name__ == "__main__":
    expressions = [
        "5 + 6 - 3",
        "7 - ( 8 * 2 )",
        "( 9 - 3 ) + ( 5 * 4 / 2 )",
        "(3 + 5 * 2 - 8) / 4 - 2 + 6",
        "86 / 2 / 3"
    ]

    generator = IntermediateCodeGenerator()

    for expression in expressions:
        print(f"Expression: {expression}")
        quadruples = generator.parse_expression(expression)
        print_quadruples(quadruples)
        print("\n" + "="*50 + "\n")
