# you need to be able to
# check if the solution is correct
# guess a value
# keep guessing until finding solution (exhaustive enumeration)

##########
# Example: guess cube root
##########

cube = -8
for guess in range(abs(cube) + 1):
    # if the guess to the power of 3 is greater than cube number it doesnt make sense to keep looking, hence the condition and the break
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    if cube < 0:
        guess = -guess
    print('Cube root of '+str(cube)+' is '+str(guess))
