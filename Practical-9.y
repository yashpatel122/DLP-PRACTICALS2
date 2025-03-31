%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(char *s);
int yylex(void);  // This is the Lex function that returns tokens.
%}

%token I T A B E

%%

S: I E T S S'    { printf("Valid string\n"); }
  | A            { printf("Valid string\n"); }
  ;

S': E S          { /* continue parsing after e */ }
   |             { /* epsilon production, nothing to do */ }
   ;

E: B             { /* continue parsing b */ }
  ;

%%

int main(void) {
    printf("Enter a string:\n");
    yyparse();
    return 0;
}

void yyerror(char *s) {
    printf("Invalid string\n");
    exit(1);
}
