Top down recursive parser used to read SML style syntax from a file and calculate the given equation
Currently limited to addition, subtraction, multiplication, and division.
Allows use of integers and floats as well as negatives.

<prog>	     ::=    <let_in_end> {let_in_end}
<let_in_end> ::=    <decl> <expr>
<decl> 	     ::=    variable <expr> <decl>
<expr>	     ::=    <term> {+ <term> | - <term>}
<term>	     ::=    <factor> {* <factor> | / <factor>}
<factor>     ::=    <expr> | variable | number | type cast variable 
