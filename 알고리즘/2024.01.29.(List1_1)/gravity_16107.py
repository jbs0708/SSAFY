import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = 0
    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if arr[i] > arr[j]:
                cnt += 1
        if max_v < cnt:
            max_v = cnt

    print(f'#{tc} {max_v}')