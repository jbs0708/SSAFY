import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def flyKill(x, y):
    global M
    global list_

    cnt = 0
    for dx in range(x, x + M):
        for dy in range(y, y + M):
            cnt += list_[dx][dy]

    return cnt


T = int(input())

for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N, M = NM[0], NM[1]

    list_ = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            max_ = max(flyKill(i,j), max_)

    print(f'#{tc} {max_}')
