def binarySearch(arr:list, ele:int):
    
    if len(arr) <= 1:
        return arr
    
    arr.sort()
    print("arr", arr)

    
    mid = len(arr)//2
    print("mid", arr[mid])

    if arr[mid] < ele:
        return binarySearch(arr[mid:], ele)
    elif arr[mid] > ele:
        return binarySearch(arr[:mid], ele)
    else:
        return f"Element found at position: {mid+1}" if len(arr) % 2 != 0 else f"Element found at position: {mid}"


output = binarySearch([12, 2, 5, 6, 1, 9], 5)
print(output)
