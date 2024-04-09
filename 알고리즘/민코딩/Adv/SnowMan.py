import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

xi = [1, -1]
yi = [1, -1]

T = 1

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    snow = (-1, -1)
    jewelry = (-1, -1)
    ans = N
    visited = [[float('inf')] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                snow = (i, j)
            if matrix[i][j] == 3:
                jewelry = (i, j)

    matrix[snow[0]][snow[1]] = 1
    q = deque()
    q.append([snow, 0, 0])

    while q:
        loc, lim, lim_max = q.popleft()

        y, x = loc

        for d in range(2):
            dx = x + xi[d]

            if 0 <= dx < M and matrix[y][dx] != 0 and matrix[y][x] != 0:
                if visited[y][dx] > lim_max:
                    visited[y][dx] = lim_max
                    q.append([(y, dx), 0, lim_max])

        for d in range(2):
            dy = y + yi[d]

            lim_max = max(lim_max, lim + 1)

            if 0 <= dy < N:
                if visited[dy][x] > lim_max:
                    visited[dy][x] = lim_max
                    if matrix[dy][x] == 0:
                        q.append([(dy, x), lim+1, lim_max])
                    else:
                        q.append([(dy, x), 0, lim_max])

    print(f'#{tc} {visited[jewelry[0]][jewelry[1]]}')
