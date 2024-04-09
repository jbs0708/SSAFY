import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def boom(y, x, ran):
    cnt = 0
    for dy in range(y-ran, y+ran+1):
        if 0 <= dy < N:
            cnt += list_[dy][x]
    for dx in range(x-ran, x+ran+1):
        if 0 <= dx < M:
            cnt += list_[y][dx]

    cnt -= list_[y][x]
    return cnt


T = int(input())

for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N, M = NM[0], NM[1]

    list_ = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0

    for i in range(N):
        for j in range(M):
            max_ = max(boom(i, j, list_[i][j]), max_)

    print(f'#{tc} {max_}')
