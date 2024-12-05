# What is a factorial ?
# Factorial is a searies in which
# 5! = 5x4x3x2x1 or 5x4! or 5x4x3x2! etc.
# Method1
def fact(n):
    if n < 1:
        return 1
    return n * fact(n-1) 

print(fact(5))

# Method2
from functools import reduce

result = reduce(lambda x, y: x * y, range(1, 6))
print(result)