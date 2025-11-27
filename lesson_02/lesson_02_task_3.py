import math

def square(x):
    s = x*x
    if not isinstance(x, int):
        return math.ceil(s)
    return s
print(square(5))
print(square(2.3))
print(square(6.4))
print(square(0.8))