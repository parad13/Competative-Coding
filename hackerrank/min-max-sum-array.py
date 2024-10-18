arr = [3, 5, 2, 1, 4]

arr.sort()

print(sum(arr[0:len(arr)-1]), sum(arr[1:]))
print(sum(arr[:-1]), sum(arr[1:]))


