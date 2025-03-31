%{
#include "y.tab.h"
%}

digit   [0-9]+(\.[0-9]+)?
%%
"("     { return LPAREN; }
")"     { return RPAREN; }
"+"     { return PLUS; }
"-"     { return MINUS; }
"*"     { return MUL; }
"/"     { return DIV; }
"^"     { return EXP; }
{digit} { yylval = atof(yytext); return NUM; }
%%
