# you need to be able to
# check if the solution is correct
# guess a value
# keep guessing until finding solution (exhaustive enumeration)

##########
# Example: guess cube root
##########

cube = -8
for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print('Cube root of '+str(cube)+' is '+str(guess))

# APPROXIMATE SOLUTIONS
# we look for a good enough solution
# start with a guess and increment by some small value
# keep guessing if |guess3-cube| >= epsilon (i.e the difference is bigger) for some small epsilon
# decreasing increment size -> means slower program
# increasing epsilon -> less accurate answer

# init variables
cube = 27
epsilon = 0.01
guess = 0.0
increment = 0.0001
num_guesses = 0
#
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
