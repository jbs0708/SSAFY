import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = 1

x0 = [1, 1]
y0 = [0, 1]

x1 = [1, 1, 0]
y1 = [0, 1, 1]

x2 = [0, 1, 0]
y2 = [0, 1, 1]

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            print(matrix[i][j],end=' ')
        print()

    q = deque()
    q.append((0, 1, 0)) # y, x, v

    while q:
        temp = q.popleft()
        y, x, v = temp[0], temp[1], temp[2]

        if v == 0:
            if x + 1 >= N or matrix[y][x+1] == 1:
                continue
            elif y+1 >= N or matrix[y+1][x] == 1:
                i = 0
                dx = x + x0[i]
                dy = y + y0[i]

                if dx < N and dy < N and matrix[dy][dx] != 1:
                    visited[dy][dx] += 1
                    q.append((dy, dx, i))

            else:
                for i in range(2):
                    dx = x + x0[i]
                    dy = y + y0[i]

                    if dx < N and dy < N and matrix[dy][dx] != 1:
                        visited[dy][dx] += 1
                        q.append((dy, dx, i))
        elif v == 1:
            if x+1 >= N or y+1 >= 0:
                if matrix[y][x+1] == 1 and matrix[y+1][x] == 1:
                    continue
            elif x+1 >= N or matrix[y][x+1] == 1:
                i = 2
                dx = x + x1[i]
                dy = y + y1[i]

                if dx < N and dy < N and matrix[dy][dx] != 1:
                    visited[dy][dx] += 1
                    q.append((dy, dx, i))

            elif y+1 >= N or matrix[y+1][x] == 1:
                i = 0
                dx = x + x1[i]
                dy = y + y1[i]

                if dx < N and dy < N and matrix[dy][dx] != 1:
                    visited[dy][dx] += 1
                    q.append((dy, dx, i))

            else:
                for i in range(3):
                    dx = x + x1[i]
                    dy = y + y1[i]

                    if dx < N and dy < N and matrix[dy][dx] != 1:
                        visited[dy][dx] += 1
                        q.append((dy, dx, i))

        elif v == 2:
            if y + 1 >= N or matrix[y+1][x] == 1:
                continue
            elif x+1 >= N or matrix[y][x+1] == 1:
                i = 2
                dx = x + x2[i]
                dy = y + y2[i]

                if dx < N and dy < N and matrix[dy][dx] != 1:
                    visited[dy][dx] += 1
                    q.append((dy, dx, i))
            else:
                for i in range(1, 3):
                    dx = x + x2[i]
                    dy = y + y2[i]

                    if dx < N and dy < N and matrix[dy][dx] != 1:
                        visited[dy][dx] += 1
                        q.append((dy, dx, i))

    print(f'#{tc} {visited[N-1][N-1]}')

    for i in range(N):
        for j in range(N):
            print(visited[i][j],end=' ')
        print()


