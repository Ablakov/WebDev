import math
a = int(input())
b = int(input())
def f(a, b):
    if (a == 1):
        return a
    if (b == 0):
        return 1
    if (b % 2 == 0):
        return f(a, b / 2) * f(a, b / 2)
    else:
        return f(a, b / 2) * f(a, b / 2) * a
    print(f(a, b))