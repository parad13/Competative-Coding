def generate_numbers():
    for i in range(5):
        yield i

# Using the generator function
numbers_generator = generate_numbers()

print(numbers_generator)

# # Iterating over the generator to get the values
# for num in numbers_generator:
#     print(num)