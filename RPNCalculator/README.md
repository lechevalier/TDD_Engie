# RPN calculator kata

An RPN calculator program computes expressions written in RPN (Reverse Polish Notation).

An RPN expression (or a postfix expression) is one of the following:
a number X, in which case the value of the expression is that of X;a sequence of the form E1 E2 O, where E1 and E2 are postfix expressions and O is an arithmetic operation; in this case, the value of the expression is that of E1 O E2.

The following are RPN expressions:

   20 5 /               => (20/5)         = 4
   
   4 2 + 3 -            => (4+2)-3        = 3
   
   3 5 8 * 7 + *        => 3*((5*8)+7)    = 141 

## Suggested scenarios

Given a RpnCalculator when a digit is sent it should display the same digit

Given a RpnCalculator when some digits are sent it should display the number formed by those digits

Given a RpnCalculator when an enter is sent between two numbers it should display the numbers separated by a newline

Given a RpnCalculator when an operation (* + / -) is sent after two numbers it should display the result of that operation