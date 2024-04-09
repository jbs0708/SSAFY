import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


xi = [1, -1, 0, 0]
yi = [0, 0, -1, 1]


def func(y, x):
    cnt = 1

    br = 0
    while br < 4:
        for d in range(4):
            dx = x + xi[d]
            dy = y + yi[d]

            if 0 <= dx < N and 0 <= dy < N and matrix[dy][dx] == matrix[y][x] + 1:
                cnt += 1
                x, y = dx, dy
                br = 0
            else:
                br += 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0
    ans = N*N

    for i in range(N):
        for j in range(N):
            sum_ = func(i, j)
            if max_ < sum_:
                max_ = sum_
                ans = matrix[i][j]
            elif max_ == sum_:
                ans = min(ans, matrix[i][j])

    print(f'#{tc} {ans} {max_}')

