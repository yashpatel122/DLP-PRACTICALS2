%{
#include <stdio.h>
#include <string.h>
int valid = 1;  /* Flag to check if the password is valid */
%}

%%

[a-z]          { valid = valid && 1; }  /* Lowercase letter */
[A-Z]          { valid = valid && 1; }  /* Uppercase letter */
[0-9]          { valid = valid && 1; }  /* Digit */
[\*\;\#\$\@]    { valid = valid && 1; }  /* Symbol */

.              { valid = 0; }  /* Any other character makes the password invalid */
{9,15}         { /* Password length between 9 and 15 */ }

%%

int main() {
    char password[100];
    scanf("%s", password);
    
    yylex();   /* Calls the lexical analyzer to process input */
    
    if (valid && strlen(password) >= 9 && strlen(password) <= 15) {
        printf("Valid password\n");
    } else {
        printf("Invalid password\n");
    }
    
    return 0;
}

int yywrap() {
    return 1;  /* End of input */
}
