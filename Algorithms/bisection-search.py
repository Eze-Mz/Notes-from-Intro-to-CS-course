# The larger the space the better is to use this bisection search method.
# With every search we eliminates halft the search space
# Half interval each iteration
# Example:
# 1 #########%%%%%%%%%%
# 2 %%%%#####
# 3     ##%%% ...etc

# initialize variables
cube = 1.5
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
# this code doesnt works with cubes < 1 without this condition, because the answer falls outside the ranges. for example 0.5**3 = 0.125.
# I'm not sure if this condition is correct.
if cube < 1:
    high = 1
guess = (high+low)/2.0
while (abs(guess**3 - cube)) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high+low)/2.0
    num_guesses += 1
print('num_guesses = ', num_guesses)
print(guess, 'is close to the cube root of', cube)
