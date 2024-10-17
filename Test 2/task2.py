import cmath
import math

def floor(num):
    if num >= 0:
        return int(num)
    if num == int(num):
        return int(num)
    return int(num) - 1


def log3(x: int):
    return int(round(x**0.5/3**0.5))

# def solver(l: int, r: int):
#     count = 0
    

for i in range(50):
    if log3(i) != math.floor(cmath.log(i, 3)):
        print(i, log3(i), math.floor(cmath.log(i, 3)))

    

# n = int(input())
# for i in range(n):
#     l = int(input())
#     r = int(input())
#     print(solver(l, r))