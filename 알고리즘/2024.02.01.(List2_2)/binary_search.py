def binary_search(arr, N, key):
    start = 0
    end = N - 1
    while start <+ end:
        middle = (start+end)//2
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1