####################
# EXAMPLE: perfect squares
####################
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
    neg_flag = True
if neg_flag:
    while ans**2 < -x:
        ans = ans + 1
    if ans**2 == -x:
        print("Square root of", x, "is", ans)
    else:
        print(x, "is not a perfect square")
else:
    while ans**2 < x:
        ans = ans + 1
    if ans**2 == x:
        print("Square root of", x, "is", ans)
    else:
        print(x, "is not a perfect square")
