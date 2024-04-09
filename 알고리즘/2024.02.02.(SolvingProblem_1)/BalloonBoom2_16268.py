import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def boom(x, y):
    cnt = -list_[x][y]
    for dx in range(x-1, x+2):
        if dx < 0 or dx >= N:
            continue
        cnt += list_[dx][y]
    for dy in range(y-1, y+2):
        if dy < 0 or dy >= M:
            continue
        cnt += list_[x][dy]

    return cnt


T = int(input())

for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N, M = NM[0], NM[1]

    list_ = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0

    for i in range(N):
        for j in range(M):
            max_ = max(boom(i, j), max_)

    print(f'#{tc} {max_}')