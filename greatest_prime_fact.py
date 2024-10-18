# #!/bin/python3


def find_factors(n):
    factors_list = []
    for i in range(1, n+1):
        if n % i == 0:
            factors_list.append(i)
    return factors_list


# Module to check if a no is a prime no
def is_prime(n):
    return len(find_factors(n)) == 2


# To print largest prime factor
t = int(input("Enter no of test cases: ").strip())
for a0 in range(t):
    n = int(input("Enter an integer: ").strip())
    max_prime_factor = 0
    allFactors = find_factors(n)
    for factor in allFactors:
        if is_prime(factor) and factor > max_prime_factor:
            max_prime_factor = factor
            
    print(f"Max prime factor is: {max_prime_factor}")
