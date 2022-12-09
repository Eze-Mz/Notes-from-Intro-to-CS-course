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