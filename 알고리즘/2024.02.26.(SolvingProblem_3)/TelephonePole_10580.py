import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]
    cross = 0

    for i in range(N-1):
        for j in range(i+1, N):
            s1, e1 = lines[i]
            s2, e2 = lines[j]

            if (s2 > s1 and e2 < e1) or (s2 < s1 and e2 > e1):
                cross += 1

    print(f'#{tc} {cross}')
