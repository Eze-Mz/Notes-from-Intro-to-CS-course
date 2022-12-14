# Types of knowledge

## Declarative
Statements of fact

## Imperative
How to --> An algorithm:
1. Sequence of simple steps
2. Flow of control process
3. A means of determining when to stop
In a mechanical process we have:
- fixed program computer (a calculator)
- stored program computer 

# Basic Machine achitecture
![basic machine architecture](/images/basic-machine-architecture.jpg)
1. Load a sequence of instructions
2. Program counter get the first instruction, counts 1 and send the instruction to the ALU
3. The ALU sees the instruction and get data from memory, do operations, put data in memory 
4. After the ALU the program the control unit goes to the next instruction
5. If the are any test instructions the control unit can jump between instructions

Stored programs are a sequence of instructions inside a cumputer *built from predefined set of primitive instructions*:
- Arithmetic and logic
- simple tests
- moving data
(the interpreter -an special program- executes each instruction in order)

## Basic primitives
```
the primitive constructs in Python include literals (3.2, "abc") and  infix operators (+, /).
```
Turing showed that you can compute anything using 6 primitives:
- Right: Move the Machine’s head to the right of the current square
- Left: Move the Machine’s head to the left of the current square
- Print: Print a symbol on the current square
- Scan: Identify any symbols on the current square
- Erase: Erase any symbols presented on the current square
- Nothing/halt: Do nothing
[video showing this](https://www.youtube.com/watch?v=gJQTFhkhwPA&ab_channel=EngMicroLectures)
Today we have a **more convenient set of primitives** and can abstract methods to create new primitives.

operations
: functions between primitives or expresiones. A programming lenguage provides a basic set of operations

expressions
: complex but legal combination of primitives, they have sintactic rules

values
: the result of expressions and computation

## Lenguages paralels

Ambos tienen sintaxis, esto quiere decir, sus elementos más pequeños requieren un orden para producir una expresión válida --> esto quiere decir, una expresión entendible. 
Que algo sea entendible, procesable, comprensible, implica la existencia de un ente capaz de entender. Para poder comprender la expresión este ente tiene que hablar o estar configurado para entender la misma sintaxis/gramática que posee la expresión.
Que algo sea entendible implica que luego de el procesamiento o entendimiento de esa expresión surge alguna especie de nuevo valor. En el caso de los programas es más simple, si las expresiones se comprenden resuelven a un valor o combinación de valores primitivos. En el caso del lenguaje es más complejo y existen varias aproximaciones a lo que es el significado.
La sintaxis puede describirse, es decir, las características que hacen comprensible al mensaje pueden analizarse. Por eso:
`uno uno uno` no tiene sentido en ninguno de los dos lenguajes y `uno más uno` o `1+1` lo tiene en ambos. En un caso se trata de la combianción de *sustantivo + conjunción copulativa + sustanvivo* y *operando + operación + operando*.

sintax
:  the syntax of a language defones which strings of characters and symbols are well formed.

static semantics
: is wich syntactically valid strings have meaning 

No estoy seguro de si en Español existe este concepto. 
"I are hungry" es el ejemplo que da. En español podría ser algo como "Yo tenemos hambre".  En todo caso es interesante el tipo de palabra es correcto, el significado es correcto, pero no la conjugación.

semantics
: is the meaning associated with a syntactically correct string of symbols with no static semantic errors.

> In programming lenguages there is only one meaning **but may not be what the programmer intended**. Programs can not be ambiguous.

# Program length
A program for which the maximum running time is bounded bye the length of the program is said to run in **constant time**: n lines of code -> n units of time to run. Exists a constant k, such that the program is guaranteed to take no mora than k steps.