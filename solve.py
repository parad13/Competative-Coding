# a = list(map(int, "34 95 34 64 45 95 16 80 80 75 3 25 75 25 31 3 64 16 31".rstrip().split()))
a = [1, 1, 2]
print(a, len(a))

def lonelyinteger(a):
    a.sort()
    for i in range(0, len(a), 2):
        # print(a, len(a))
        # print(len(a) == 1)
        c = a[i]
        if len(a) == 1:
            return a[i]
        elif i+1 == len(a):
            break
        elif a[i] != a[i+1]:
            b = a[i+1]
            return a[i]
            
print(lonelyinteger(a))

# i j
# 0 1
# 2 3
# 4 5
# 6 7
# 8 9
# 10 11
# 12 13
# 14 15
# 16 17
# 18 19
