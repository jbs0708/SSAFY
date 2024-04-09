import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def selection_sort(a, N):
    for i in range(N-1):
        if i % 2 == 1:
            min_idx = i
            for j in range(i+1, N):
                if a[min_idx] > a[j]:
                    min_idx = j
            a[min_idx], a[i] = a[i], a[min_idx]
        else:
            max_idx = i
            for j in range(i + 1, N):
                if a[max_idx] < a[j]:
                    max_idx = j
            a[max_idx], a[i] = a[i], a[max_idx]
    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))

    selection_sort(n_list, N)

    print(f'#{tc} ', end='')
    for i in range(10):
        print(f'{n_list[i]} ',end='')
    print()

