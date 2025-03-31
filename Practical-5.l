%{
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int line_num = 1;   /* Line number tracking */
FILE *source_code;  /* Input file for the source code */

void print_token(char *type, char *token) {
    printf("%s: %s\n", type, token);
}

%}

%%

/* Regular expressions for tokens */

"int"|"char"|"return"|"void"|"long"|"float"|"double"    { print_token("Keyword", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*    { print_token("Identifier", yytext); }

[0-9]+                     { print_token("Constant", yytext); }
\"[^\"]*\"                 { print_token("String", yytext); }

"(" | ")" | "{" | "}" | ";" | ","    { print_token("Punctuation", yytext); }
"\+" | "\-" | "\*" | "/" | "=" | "==" | "!=" | "<" | ">" | "<=" | ">="   { print_token("Operator", yytext); }

/* Comments */
"//".*    { /* Skip single-line comments */ }
"/\*"[^*]*"\*/"    { /* Skip multi-line comments */ }

/* Invalid lexemes */
[^a-zA-Z0-9_;\+\-\*/\(\){}\[\]=<>!&|^"\'\n]    { 
    printf("LEXICAL ERROR: Line %d: %s invalid lexeme\n", line_num, yytext); 
}

/* Track line number */
\n          { line_num++; }

%%

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Usage: %s <source code file>\n", argv[0]);
        return 1;
    }

    /* Open the C source code file */
    source_code = fopen(argv[1], "r");
    if (source_code == NULL) {
        printf("Error opening file %s\n", argv[1]);
        return 1;
    }

    yyin = source_code; /* Assign input file */
    yylex();  /* Process input using Lex */
    
    fclose(source_code);  /* Close the file after processing */
    return 0;
}

int yywrap() {
    return 1;
}
