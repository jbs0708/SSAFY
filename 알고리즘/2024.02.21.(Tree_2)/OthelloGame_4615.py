import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def check(y, x, bw):
    wb = 0
    if bw == 1:
        wb = 2
    else:
        wb = 1

    for d in range(8):
        q = deque()
        dx = x
        dy = y
        while True:
            dx += xi[d]
            dy += yi[d]
            if 0 <= dx < N and 0 <= dy < N:
                if matrix[dy][dx] == wb:
                    q.append((dy, dx))

                if matrix[dy][dx] == 0:
                    break

                if matrix[dy][dx] == bw and q:
                    while q:
                        ny, nx = q.popleft()
                        matrix[ny][nx] = bw
                    matrix[y][x] = bw
                    break

                if matrix[dy][dx] == bw and not q:
                    break
            else:
                break


T = int(input())

xi = [1, 0, -1, 0, 1, 1, -1, -1]
yi = [0, -1, 0, 1, 1, -1, 1, -1]

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]

    mid = N//2 - 1
    matrix[mid][mid] = 2
    matrix[mid][mid+1] = 1
    matrix[mid+1][mid] = 1
    matrix[mid+1][mid+1] = 2

    for m in range(M):
        x, y, bw = map(int, input().split())
        x -= 1
        y -= 1
        if matrix[y][x] == 0:

            check(y, x, bw)

    b = 0
    w = 0
    for i in range(N):
        b += matrix[i].count(1)
        w += matrix[i].count(2)

    print(f'#{tc} {b} {w}')
