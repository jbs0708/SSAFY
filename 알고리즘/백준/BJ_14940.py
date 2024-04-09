import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

NM = list(map(int, input().split()))
N = NM[0]
M = NM[1]

map_list = [list(map(int, input().split())) for _ in range(N)]
d_list = [[(N*M) for i in range(M)] for _ in range(M)]
visit = [[-1] * M for _ in range(N)]

xi = [-1, 1, 0, 0]
yi = [0, 0, 1, - 1]

def bfs_(x,y):
    q = deque()
    q.append((x,y))

    visit[x][y] = 0

    while q:
        dx, dy = q.popleft()

        for i in range(4):
            nx, ny = dx+xi[i], dy+yi[i]

            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == -1:
                if map_list[nx][ny] == 0:
                    visit[nx][ny] = 0
                elif map_list[nx][ny] == 1:
                    visit[nx][ny] = visit[dx][dy] + 1
                    q.append((nx, ny))

for i in range(N):
    for j in range(M):
        if map_list[i][j] == 2 and visit[i][j] == -1:
            bfs_(i, j)

for i in range(N):
    for j in range(M):
        if map_list[i][j] == 0:
            print(map_list[i][j], end=' ')
        else:
            print(visit[i][j], end=' ')
    print()

