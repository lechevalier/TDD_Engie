# FooBarQix

## Divisor rule:
If the following digit divides `n`,
return its associated string.

## Content rule:
If the following digit is inside `n`,
return its associated string.

## Digits and associated strings:

1. 3 -> "Foo"
2. 5 -> "Bar"
3. 7 -> "Qix"

## Description
For a given number:
- Try to apply divisor rule first.  
- If not applied, try to apply content rule.  
- Otherwise return its string representation.

Each digit rule applies in listed order.  
Divisor rule applies first.
