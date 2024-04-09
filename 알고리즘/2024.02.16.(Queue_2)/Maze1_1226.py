import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

xi = [0, 1, 0, -1]
yi = [1, 0, -1, 0]

def bfs(y, x, visited):
    visited[y][x] = True

    for d in range(4):
        dx = x + xi[d]
        dy = y + yi[d]

        if 1 <= dx < N-1 and 1 <= dy < N-1 and not visited[dy][dx] and maze[dy][dx] != '1':
            bfs(dy, dx, visited)


T = 10

for tc in range(1, T + 1):
    t = input()
    N = 16
    maze = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    visited[1][1] = visited

    ax, ay = -1, -1
    for i in range(1, N-1):
        for j in range(1, N-1):
            if maze[i][j] == '3':
                ax = j
                ay = i

    bfs(1, 1, visited)

    print(f'#{tc} {visited[ay][ax] + 0}')



