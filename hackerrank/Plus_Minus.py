arr = [-4, 3, -9, 0, 4, 1]

# # try1 - step1 - trying to take the input
# n = input("Enter array length: ")
# arr = list(map(int, input("Enter array elements: ")))

# print(n)
# print(arr)

# # print("{}\n{}".format(n, arr))

# # three var for caching count of pos, neg and zero


pos, neg, zero = 0, 0, 0
# try2 - step1
for i in arr:
    if i > 0: pos += 1
    elif i<0: neg += 1
    else: zero+=1

print(format(pos/len(arr),".6f"), format(neg/len(arr),".6f"), format(zero/len(arr),".6f"))
