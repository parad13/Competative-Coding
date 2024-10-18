# Problem - Filter even numbers in given list and double them 
arr = [4, 7, 2, 5, 1, 3, 4, 7, 2, 5, 1, 3, 6, 8, 10]


# even_no_list = list(filter(lambda x: x%2 == 0, arr))
# print("Even no list: ", even_no_list)

# doubled_even_no_list = list(map(lambda x: x*2, even_no_list))
# print("doubled_even_no_list: ", doubled_even_no_list)


doubled_even_no_list = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, arr)))
print("doubled_even_no_list: ", doubled_even_no_list)

# array = [8, 3, 4, 2, 3, 5, 1, 8, 4, 6]


# even_array = list(filter(lambda x : x % 2 == 0, array))

# print(even_array)

# double_array = list(map(lambda x:x*2, even_array))

# print(double_array)

## Reduce
# from functools import reduce

# sum_of_double_array = reduce(lambda a,b : a+b, double_array)

# print(sum_of_double_array)

# print(reduce(lambda a,b : a+b, list(map(lambda x:x*2, list(filter(lambda x : x % 2 == 0, array))))))

