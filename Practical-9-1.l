%{
#include "y.tab.h"
%}

i      { return I; }
t      { return T; }
a      { return A; }
b      { return B; }
e      { return E; }
\n     { return 0; }

%%
