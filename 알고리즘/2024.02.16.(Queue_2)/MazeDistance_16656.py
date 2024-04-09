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
    visited = [[0] * N for _ in range(N)]

    y, x = -1, -1
    for i in range(N):
        found = False
        for j in range(N):
            if matrix[i][j] == '2':
                y = i
                x = j
                found = True
                break
        if found:
            break

    q = deque()
    q.append((y, x))

    v = 0
    max_ = 0
    found = False
    while q:
        v += 1
        q_list = []
        while q:
            q_list.append(q.popleft())
        next_q = deque()
        for point_ in q_list:
            temp = point_
            dy = temp[0]
            dx = temp[1]
            visited[dy][dx] = v

            if matrix[dy][dx] == '3':
                max_ = v - 2
                found = True
            else:
                for d in range(4):
                    nx = dx + xi[d]
                    ny = dy + yi[d]

                    if 0 <= nx < N and 0 <= ny < N and matrix[ny][nx] != '1' and visited[ny][nx] == 0:
                        next_q.append((ny, nx))

        if found:
            break
        else:
            q = next_q

    print(f'#{tc} {max_}')