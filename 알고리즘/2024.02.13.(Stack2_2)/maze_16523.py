import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

xi = [0, 0, 1, -1]
yi = [1, -1, 0, 0]

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    s = ()
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        found = False
        for j in range(N):
            if matrix[i][j] == '2':
                s = (i, j)
                found = True
                break
        if found:
            break

    q = deque([s])

    found = False
    while q:
        loc = q.pop()

        for i in range(4):
            dx = loc[1] + xi[i]
            dy = loc[0] + yi[i]

            if 0 <= dx < N and 0 <= dy < N and matrix[dy][dx] != '1' and not visited[dy][dx]:
                visited[dy][dx] = True
                if matrix[dy][dx] == '3':
                    found = True
                    break
                else:
                    q.append((dy, dx))
                    # # 프린터
                    # print((dy, dx))
                    # matrix[dy][dx] = 'v'
                    # for i in range(N):
                    #     for j in range(N):
                    #         print(matrix[i][j], end=' ')
                    #     print()
                    # print()
                    # # 프린터

        if found:
            break

    if found:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')