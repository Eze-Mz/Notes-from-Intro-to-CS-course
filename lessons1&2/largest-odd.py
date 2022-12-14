# the code start with a provisional value to the answer (the min if no there is no odd numbers)
x, y, z = 1, 3, 5
answer = min(x, y, z)
if x % 2 != 0:
    answer = x
if y % 2 != 0 and y > answer:
    answer = y
if z % 2 != 0 and z > answer:
    answer = z
print(answer)

x = y if y > z else z

print(x)
