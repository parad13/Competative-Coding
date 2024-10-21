def quick_sort(arr:list) -> list:

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]


    left = [ele for ele in arr[:-1] if ele <= pivot]
    right = [ele for ele in arr[:-1] if ele > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
    arr = list(map(int, input("Enter your array to sort: ").rstrip().split()))
    # arr = list(map(int, input("Enter your array to sort: ").strip().split(" "))) # Logic to remove empty spaces
    # arr = [10, 7, 8, 9, 1, 5]
    # print(arr)
    output = quick_sort(arr)
    print("Sorted array:", output)
    # Ans = [1, 5, 7, 8, 9, 10]

    