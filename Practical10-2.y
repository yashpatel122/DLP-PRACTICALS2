%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void yyerror(char *s);
int yylex(void);

%}

%token LPAREN RPAREN PLUS MINUS MUL DIV EXP NUM

%left PLUS MINUS
%left MUL DIV
%right EXP

%%

L: E { printf("%.2f\n", $1.val); }
;

E: E PLUS T { $$.val = $1.val + $3.val; }
  | E MINUS T { $$.val = $1.val - $3.val; }
  | T { $$.val = $1.val; }
  ;

T: T MUL F { $$.val = $1.val * $3.val; }
  | T DIV F { $$.val = $1.val / $3.val; }
  | F { $$.val = $1.val; }
  ;

F: G EXP F { $$.val = pow($1.val, $3.val); }
  | G { $$.val = $1.val; }
  ;

G: LPAREN E RPAREN { $$.val = $2.val; }
  | NUM { $$.val = $1; }
  ;

%%

int main(void) {
    printf("Enter an arithmetic expression:\n");
    yyparse();
    return 0;
}

void yyerror(char *s) {
    printf("Invalid expression\n");
    exit(1);
}
