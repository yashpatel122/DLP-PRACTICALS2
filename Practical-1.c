#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Function to validate the input string against the pattern a*bb
bool isValidString(const char *str) {
    int i = 0;
    int len = strlen(str);
    
    // Allow leading 'a' characters
    while (i < len && str[i] == 'a') {
        i++;
    }
    
    // Ensure the last two characters are 'b'
    if (i < len - 1 && str[i] == 'b' && str[i + 1] == 'b' && i + 2 == len) {
        return true;
    }
    
    return false;
}

int main() {
    char input[100];
    
    printf("Enter a string: ");
    fgets(input, sizeof(input), stdin);
    
    // Remove newline character if present
    size_t len = strlen(input);
    if (len > 0 && input[len - 1] == '\n') {
        input[len - 1] = '\0';
    }
    
    if (isValidString(input)) {
        printf("Valid String\n");
    } else {
        printf("Invalid String\n");
    }
    
    return 0;
}
