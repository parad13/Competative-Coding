# Standard way
def take_input():
    # Take input from the user
    user_input = input("Enter numbers separated by spaces: ")
    # Split the input string into a list of strings
    input_list = user_input.split()
    # Convert the list of strings to a list of integers
    numbers = [int(num) for num in input_list]
    return numbers

# Example usage
numbers_list = take_input()
print("You entered:", numbers_list)

# python one liner
arr = list(map(int, input().split()))
print(arr)