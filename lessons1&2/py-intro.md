Everything is a data object
Data object have a type that defines what can do
Objects are: 
- SCALAR (cannot be subdivided) 
- NON SCALAR (have internal structure that can be accesed)

# SCARLAR OBJECTS
- int -> integers
- float -> real numbers 
- bool -> boolean values
- NoneType -> special and has one value: *None*
> we can use type() function to check the type 

## Type conversions
- float(3) -> integer to float #3.0
- int(3.9) -> truncate float 3.9 to integer 3

# Expressions
Combine objects and operators. Evaluates to a value that has a type. 
Syntax for a simple expression:
```<object><operator><object>```

# Operators on ints and floats
- i + j -> return int or float
- i - j -> return int or float
- i * j -> return int or float
- i / j -> return float
- i % j -> remainder
- i ** j -> i to the power of j

> Same precedence that in mathematics

# Assignment
- equal sign is an assignment of a value to a variable name
- value stored in computer memory
- an assignment binds name to value
- invoking the variable retrieves the value

**In math the equal symbol stands for equivalence, not assignment**

When we rebind a variable, the previous value may still stored in memory (until garbage collector removes it) but los the handle for it.
## Multiple assignment
x, y = 2, 3
Allows to swap bindings:
x, y = y, x --> now x is 3 and y is 2

# Comparison operators (on int, float and string)
- i > j
- i >= j
- i < j
- i <= j
- i == j
- i != j

# Logic operators
- not
- and
- or

# Control flow - if
``` 
if <condition>:
<expression>
<expression>
...
elif <condition>:
<expression>
<expression>
...
else:
<expression>
<expression>
...
```
## Conditional expressions
"*expr1* if *condition* else *expr2*"
x = y if y > z else z

# Constrol flow - while loop
``` 
while <condition>:
<expression>
<expression>
...
``` 

# Control flow - for loop
```
for <variable> in range(<some_num>):
<expression>
<expression>
...
```
- range(start,stop,step)
- default values are start = 0 and step = 1 and optional
-  loop until value is stop - 1 

range is a way to iterate over numbers, but a for loop
variable can iterate over any set of values, not just numbers!
*for index in range(len(s)):* vs *for char in s:*

# Break statement
- immediately exits whatever loop it is in
- skips remaining expressions in code block
- exits only innermost loop!

# Strings
strings are “immutable” – cannot be modified

## f-strings
Formatted string literal, consists of the character f before the string. This format can contain expressions inside curly braces:
```
print(f'{int(6*1/2)} is {1/2*100}% of {6}')
```
These expressions are evaluated at runtime and converted to strings.
### Modifiers
The expression inside an f-string can contain modifiers that control the appearance of the output string, the modifiers is separated from the expression by a colon:
f'{3.14159: .2f}' -> truncates the number

## Encoding
You can tell Python the encoding:
```python
# -*- coding: encoding name  -*-
```