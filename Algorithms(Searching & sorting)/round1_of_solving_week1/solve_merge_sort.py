def MergeSort(arr: list) -> list:
    # Base case if arr has one element, no need to sort just return it
    if len(arr) <= 1:
        return arr

    # Divide array in two equal half
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    # print(mid, left, right)

    # Calling recursion
    left_sorted = MergeSort(left)
    right_sorted = MergeSort(right)

    return Merge(left_sorted, right_sorted)

def Merge(left:list, right:list) -> list:
    # print("left", left, "right", right)
    i = 0
    j = 0
    output = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j] :
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    while i < len(left):
        output.append(left[i])
        i += 1
    
    while j < len(right):
        output.append(right[j])
        j += 1
    
    # print("Output", output)

    return output


if __name__  == "__main__":
    arr = list(map(int, input("Enter an array to sort: ").rstrip().split()))
    # arr = [10, 7, 8, 9, 1, 5]
    output = MergeSort(arr)
    print("Sorted array: ", output)
    # Ans - [1, 5, 7, 8, 9, 10]
    



    