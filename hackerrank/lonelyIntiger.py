# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example
# a = [1, 2, 3, 4, 3, 2, 1]
# The unique element is 4.

# Solved using a dict for string count of val


def lonelyinteger(a):
    dic = {}
    
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    
    for k, v in dic.items():
        if v == 1:
            return k
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    a = list(map(int, input().rstrip().split()))
  
    result = lonelyinteger(a)