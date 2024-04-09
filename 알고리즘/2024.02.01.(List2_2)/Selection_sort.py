def selection_sort(a, N):
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if a[min_idx] > a[j]:
                min_idx = j
        a[min_idx], a[i] = a[i], a[min_idx]
    return

N = 5
arr = [1, 3, 2, 5, -2]
print(arr)
selection_sort(arr, N)
print(arr)