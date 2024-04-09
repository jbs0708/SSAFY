import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    list_ = list(map(int, input().split()))

    min_id = N+1
    min_val = 11
    max_id = -1
    max_val = 0

    for n in range(N):
        if list_[n] < min_val:
            min_id = n
            min_val = list_[n]
        if list_[n] >= max_val:
            max_id = n
            max_val = list_[n]

    max_ = abs(max_id - min_id)

    print(f'#{tc} {max_}')