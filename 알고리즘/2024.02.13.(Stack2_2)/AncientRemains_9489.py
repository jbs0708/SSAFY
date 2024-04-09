import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def dfs_row(y, x, visited, cnt):
    global max_
    visited[y][x] = True
    for i in range(2):
        dx = x + xi_row[i]
        if 0 <= dx < M and matrix[y][dx] == 1 and not visited[y][dx]:
            cnt += 1
            dfs_row(y, dx, visited, cnt)

    max_ = max(max_, cnt)
    return

def dfs_col(y, x, visited, cnt):
    global max_
    visited[y][x] = True
    for i in range(2):
        dy = y + yi_col[i]
        if 0 <= dy < N and matrix[dy][x] == 1 and not visited[dy][x]:
            cnt += 1
            dfs_col(dy, x, visited, cnt)

    max_ = max(max_, cnt)
    return


T = int(input())

xi_row = [-1, 1]
yi_col = [-1, 1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    visited_r = [[False] * M for _ in range(N)]
    visited_c = [[False] * M for _ in range(N)]
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0

    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1 and not visited_r[y][x]:
                dfs_row(y, x, visited_r, 1)
            if matrix[y][x] == 1 and not visited_c[y][x]:
                dfs_col(y, x, visited_c, 1)

    print(f'#{tc} {max_}')

