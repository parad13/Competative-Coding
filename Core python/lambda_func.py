# Normal way to finding a square using class
class square:
    def __init__(self):
        self.x = 1
    
    def __call__(self, x):
        return x * x

square_class_instance = square()

print("o/p from class: ", square_class_instance(5))
print("o/p from class: ", square_class_instance(square_class_instance(5)))

# Normal way to finding a square using function
def squarefn(x):
    return x*x

print("o/p from function: ", squarefn(6))

# Using lambda function
square_lam = lambda x: x*x

print("o/p from lambda function: ", square_lam(7))

# Finding/ squaring a list using class and a lambda function
print(list(map(square(), [1, 2, 3])))
print(list(map(lambda y: y**2, [3, 4, 5])))