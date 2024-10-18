# What is a factorial ?
# Factorial is a searies in which
# 5! = 5x4x3x2x1 or 5x4! or 5x4x3x2! etc.
def fact(n):
    if n < 1:
        return 1
    return n * fact(n-1) 

print(fact(5))