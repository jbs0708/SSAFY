import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    cnt = 0
    for i in range(-N, N+1):
        for j in range(-N, N+1):
            if (i*i) + (j*j) <= (N*N):
                cnt += 1

    print(f'#{tc} {cnt}')