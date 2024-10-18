# Q. Search given val in given arr
# arr = [5, 7, 9, 12, 17]
# val = 12

def linear_search(arr, target):
    # Loop through each element in the array
    for i in range(len(arr)):
        # check if the current element matches the target
        if arr[i] == target:
            return i # Return the index if found
    return -1 # Return -1 if the target is not found

if __name__ == "__main__":
    # Need to learn
    # arr = list(map(int, input().rstrip().split()))
    # val = int(input().strip())

    result = linear_search(arr, val)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")