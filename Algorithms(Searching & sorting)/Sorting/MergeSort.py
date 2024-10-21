def merge_sort(arr):
    # print("arr1", arr)
    # Base case: if the array has one or no elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively split and sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)

    # print("Output:", output)

def merge(left, right):
    # print("left:", left, "right:", right)
    merged = []
    # Take two pointers i & j
    i = 0
    j = 0
    
    # Compare elements from both halves and add the smaller one to the merged list
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add any remaining elements from the left half
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Add any remaining elements from the right half
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

if __name__ == "__main__":
    # Example 
    # arr = list(map(int, input().rstrip().split()))
    arr = [10, 7, 8, 9, 1, 5]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
