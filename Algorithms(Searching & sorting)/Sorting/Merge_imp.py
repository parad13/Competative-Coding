def Merge(left:list, right:list) -> list:
    i = 0
    j = 0
    merged_arr = []
    len_left = len(left)
    len_right = len(right)

    while i < len(left) and j < len(right):
        a = left[i]
        b = right[j]
        if left[i] <= right[j] :
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1

    while i < len(left):
        c = left[i]
        merged_arr.append(left[i])
        i += 1
    
    while j < len(right):
        d = right[j]
        merged_arr.append(right[j])
        j += 1

    return merged_arr

print(Merge([3, 4, 1], [2, 5]))