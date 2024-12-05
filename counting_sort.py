def countingSort(arr):
    freq_arry = [0] * (max(arr)+1)
    # freq_arry = [0] * (max(arr)+1 if max(arr)+1 > 100 else 100)
    arr.sort()
    for i in arr:
        freq_arry[i] += 1
        
    return freq_arry


frequency_array = countingSort([1, 3, 5, 2, 5, 2, 5, 2, 5, 8])
print("Frequency array: ", frequency_array)


# create the sorted array from the frequency_array
original_array = []

for value, count in enumerate(frequency_array):
    original_array.extend([value] * count) 

print(original_array)