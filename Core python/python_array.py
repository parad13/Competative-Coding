"""
Consider an array arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

Basic slicing:

arr[1:5] will give [1, 2, 3, 4]. (Starts at index 1 and ends just before index 5.)
Omitting start or stop:

arr[:5] gives [0, 1, 2, 3, 4] (starts from the beginning and stops before index 5).
arr[5:] gives [5, 6, 7, 8, 9] (starts from index 5 to the end of the array).
Using step:

arr[::2] gives [0, 2, 4, 6, 8] (every second element from the start).
arr[1:8:2] gives [1, 3, 5, 7] (starts at index 1, ends before 8, with a step of 2).
Negative step:

arr[::-1] gives [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverses the array).
arr[8:3:-1] gives [8, 7, 6, 5, 4] (slices from index 8 down to index 4 in reverse).
Summary:
[start:] slices from start to the end.
[:stop] slices from the beginning to stop (exclusive).
[::step] slices the whole array with a step size.
[::-1] reverses the array.
Each of these components (start, stop, and step) can be mixed and matched to perform complex slicing on arrays or lists.
"""

# array[start:stop:step]

arr = [3, 5, 2, 1, 4]
arr.sort() #will sort the array