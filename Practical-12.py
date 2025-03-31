import re

# Function to evaluate simple constant expressions
def evaluate_constant_expression(expression):
    try:
        # Try evaluating the expression using Python's eval function (safe for simple arithmetic)
        return str(eval(expression))
    except Exception as e:
        # Return the original expression if evaluation fails (due to variables)
        return expression

# Function for constant folding optimization
def constant_folding(expression):
    # Regular expression to match arithmetic expressions with constants
    # This will match simple constant subexpressions, e.g., 2 + 3, 5 * 10, etc.
    pattern = r'(\d+(\.\d+)?)\s*([-+*/^])\s*(\d+(\.\d+)?)'
    
    # Continuously replace constant subexpressions with their evaluated result
    while re.search(pattern, expression):
        # Find the first constant expression match
        match = re.search(pattern, expression)
        
        # Extract the matched components
        operand1, _, operator, operand2 = match.groups()
        
        # Form the subexpression
        subexpr = f"{operand1} {operator} {operand2}"
        
        # Evaluate the constant subexpression
        evaluated_result = evaluate_constant_expression(subexpr)
        
        # Replace the subexpression with the evaluated result
        expression = expression.replace(subexpr, evaluated_result, 1)
    
    return expression

# Driver code to test the constant folding
if __name__ == "__main__":
    expressions = [
        "5 + x - 3 * 2",            # Example with variables
        "2 + 3 * 4 - 1",            # Constant folding example
        "x + (3 * 5) - 2",          # Constant folding with parentheses
        "(22 / 7) * r * r",         # Constant folding with division
        "3 + (2 * 5) - 4 / 2",      # More complex constant folding
    ]
    
    for expr in expressions:
        print(f"Original Expression: {expr}")
        optimized_expr = constant_folding(expr)
        print(f"Optimized Expression: {optimized_expr}\n")
