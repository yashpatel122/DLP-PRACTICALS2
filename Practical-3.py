import re

# Define token categories
KEYWORDS = {"int", "char", "return", "void", "struct", "long", "float"}
OPERATORS = {"=", "+", "-", "*", "/", "%"}
PUNCTUATIONS = {"(", ")", "{", "}", ",", ";"}
IDENTIFIER_PATTERN = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")
CONSTANT_PATTERN = re.compile(r"^\d+$")

# Function to remove comments
def remove_comments(code):
    code = re.sub(r"//.*", "", code)  # Remove single-line comments
    code = re.sub(r"/\*.*?\*/", "", code, flags=re.DOTALL)  # Remove multi-line comments
    return code

# Lexical Analyzer function
def lexical_analyzer(code):
    code = remove_comments(code)
    lines = code.split("\n")
    symbol_table = set()
    tokens = []
    errors = []
    
    for line_no, line in enumerate(lines, start=1):
        words = re.findall(r"\w+|\S", line)
        
        for word in words:
            if word in KEYWORDS:
                tokens.append(("Keyword", word))
            elif word in OPERATORS:
                tokens.append(("Operator", word))
            elif word in PUNCTUATIONS:
                tokens.append(("Punctuation", word))
            elif CONSTANT_PATTERN.match(word):
                tokens.append(("Constant", word))
            elif IDENTIFIER_PATTERN.match(word):
                tokens.append(("Identifier", word))
                symbol_table.add(word)
            else:
                errors.append((line_no, word))
    
    return tokens, symbol_table, errors

# Function to read input file and analyze
def main():
    file_path = input("Enter the path of the C source code file: ")
    with open(file_path, "r") as file:
        code = file.read()
    
    tokens, symbol_table, errors = lexical_analyzer(code)
    
    print("\nTOKENS")
    for token in tokens:
        print(f"{token[0]}: {token[1]}")
    
    print("\nSYMBOL TABLE ENTRIES")
    for i, identifier in enumerate(symbol_table, start=1):
        print(f"{i}) {identifier}")
    
    if errors:
        print("\nLEXICAL ERRORS")
        for line_no, word in errors:
            print(f"Line {line_no}: {word} invalid lexeme")
    else:
        print("\nNo lexical errors found.")

if __name__ == "__main__":
    main()
