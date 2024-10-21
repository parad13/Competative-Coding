# Recursion limit in Python 998 can be called 
def find_factorial(n:int) -> int:
    print(n)
    if n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial(n-1)

output = find_factorial(int(input("Enter a no. to find factorial: ")))
print(output)