import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


xi = [1, 0]
yi = [0, 1]


def dfs(y, x, temp):
    global sum_

    if x == N-1 and y == N-1:
        sum_ = min(sum_, temp)
        return

    for d in range(2):
        dx = x + xi[d]
        dy = y + yi[d]
        if dx < N and dy < N:
            temp += matrix[dy][dx]
            dfs(dy, dx, temp)
            temp -= matrix[dy][dx]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sum_ = float('inf')

    dfs(0, 0, matrix[0][0])

    print(f'#{tc} {sum_}')

