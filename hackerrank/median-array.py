def findMedian(arr):
    arr.sort()
    return arr[len(arr)//2]

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)
    print(result)