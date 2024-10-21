def quick_sort(arr):

    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (here, the last element of the array)
    pivot = arr[-1]
    
    # Partition the array into left (less than pivot) and right (greater than pivot)
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # print("left:", left, "right:", right, "pivot:", pivot)
    
    # Recursively sort the left and right partitions and combine them
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
# Ans - [1, 5, 7, 8, 9, 10]
