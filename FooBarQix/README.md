# FooBarQix

## Divisor rule:
If the following digit divides `n`,
add its associated string to the result.

## Content rule:
For each occurrence of following digit inside `n`,
add its associated string to the result.

## Digits and associated strings:

1. 3 -> "Foo"
2. 5 -> "Bar"
3. 7 -> "Qix"

## Description
For a given number:
- Apply divisor rule.  
- Apply content rule.  
- If result is empty, return its string representation.

Each digit rule applies in listed order.  
Divisor rule applies first.
