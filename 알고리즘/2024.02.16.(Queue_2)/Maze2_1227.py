import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = 10

for tc in range(1, T + 1):
    t = input()
    N = 100
    maze = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    visited[1][1] = visited

    ax, ay = -1, -1
    for i in range(1, N-1):
        for j in range(1, N-1):
            if maze[i][j] == '3':
                ax = j
                ay = i

    q = deque()
    q.append([1, 1])

    xi = [0, 1, 0, -1]
    yi = [1, 0, -1, 0]

    while q:
        y, x = q.popleft()

        for d in range(4):
            dx = x + xi[d]
            dy = y + yi[d]

            if 1 <= dx < N - 1 and 1 <= dy < N - 1 and not visited[dy][dx] and maze[dy][dx] != '1':
                visited[dy][dx] = True
                q.append([dy, dx])

    print(f'#{tc} {visited[ay][ax] + 0}')



