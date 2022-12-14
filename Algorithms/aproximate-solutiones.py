# APPROXIMATE SOLUTIONS
# we look for a good enough solution
# start with a guess and increment by some small value
# keep guessing if |guess3-cube| >= epsilon (i.e the difference is bigger) for some small epsilon (because the solution its not good enough)
# you can change epsilon and the increment value
# decreasing increment size -> means slower program
# increasing epsilon -> less accurate answer

# init variables
cube = 23580
epsilon = 0.1
guess = 0.0
increment = 0.0001
num_guesses = 0
# The code has a bug -> if the increment doesnt make the difference fall into the epsilon range, the code will run forever.
# if epsilon if too small the difference may never be in range
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)
