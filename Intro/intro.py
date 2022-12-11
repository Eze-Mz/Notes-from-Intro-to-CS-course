# print(type(5))
# print(type(False))
# print(type(None))

pi = 3.14
radius = 2.2
area = pi * (radius ** 2)
print(int(area))

# Implement the algorithm of Heron of Alexandria to compute the square root of a number
# https://www.hellenicaworld.com/Greece/Science/en/HeronsMath.html

##### String object type #####
# concatenate strings
hi = "hello there"
name = "ana"
greet = hi + name
greeting = hi + " " + name
print(greeting)

# star * operator -> on strings repeat the string n times
silly = hi + " " + name * 3
print(silly)

# str() -> convert number in string
x = 1
print(type(x))
x_str = str(x)
print(type(x_str))

# input() -> function that prints the argument and then waits for the user to type something and hit enter. Returns a string
#nombre = input("Escribe tu nombre: ")
#print("hola " + nombre)

##### Control flow - if #####
x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    print("numbers are equal!")
elif x > y:
    print("y is smaller!")
else:
    print("x is smaller!")

# conditional expression
z = 1
x = y if y > z else z
print(x)


##### Control flow - while loop #####
n = input("You're in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You're in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")

##### Control flow - for loop #####
#sintax: range(start,stop,step)
# default values are start = 0 and step = 1 and optional
# loop until value is stop - 1
mysum = 0
for i in range(7, 10):
    mysum += i
print(mysum)  # 7+8+9 = 24

mysum = 0
for i in range(5, 11, 2):
    mysum += i
print(mysum)  # 5+7+9 = 21

##### String manipulation #####
# len() ->   is a function used to retrieve the length of the string in the parentheses
len("hello")  # 5

# square brackets used to perform indexing into a string to get the value at a certain index/position
str = "abc"
str[0]  # a
str[1]  # b
str[2]  # c
str[-1]  # c

# sintax of the indexing
# can slice strings using [start:stop:step]
# if give two numbers, [start:stop], step=1 by default
# you can also omit numbers and leave just colons
str[::]  # returns the same string
str[::-1]  # cba -> reverse the string same as str[-1:-(len(s)+1):-1]
