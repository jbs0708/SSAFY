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
    N, M = map(int, input().split())

    list_ = [list(map(int, input().split())) for _ in range(N)]
    min_ = M*M*30

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = flyKill(i, j)
            if temp % 2 == 0:
                if min_ > temp:
                    min_ = temp

    print(f'#{tc} {min_}')
