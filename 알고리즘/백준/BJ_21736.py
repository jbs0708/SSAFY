from collections import deque

NM = list(map(int, input().split()))
N = NM[0]
M = NM[1]
# 얕은 복사 오류
# visit = [[False] * M] * N
visit = [[False for _ in range(M)] for _ in range(N)]
cnt = 0
start = ()

map_list = []
for i in range(N):
    temp = input()
    map_list.append(temp)
    for j in range(M):
        if temp[j] == 'I':
            start = (i,j)
            visit[i][j] = True
        if temp[j] == 'X':
            visit[i][j] = True

xi = [-1, 1, 0, 0]
yi = [0, 0, 1, - 1]

q = deque([start])
while(q):
    dx, dy = q.popleft()

    for i in range(4):
        nx, ny = dx+xi[i], dy+yi[i]

        if 0 <= nx < N and 0 <= ny < M:
            if not visit[nx][ny]:
                q.append((nx,ny))
                visit[nx][ny] = True
                if map_list[nx][ny] == 'P':
                    cnt += 1


if cnt > 0:
    print(cnt)
else:
    print('TT')
