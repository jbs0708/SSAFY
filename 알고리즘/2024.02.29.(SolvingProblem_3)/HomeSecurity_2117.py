import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

xi = [0, 1, 0, -1]
yi = [-1, 0, 1, 0]


def searching(K, visited, cost, q, homes):
    global ans
    # print(f'K: {K}, homes: {homes}, cost: {cost}')

    if cost >= 0 and ans < homes:
        ans = homes

    new_q = deque()
    K += 1

    while q:
        y, x = q.popleft()

        for d in range(4):
            dx = x + xi[d]
            dy = y + yi[d]

            if 0 <= dx < N and 0 <= dy < N and not visited[dy][dx]:
                visited[dy][dx] = 1
                new_q.append((dy, dx))
                if matrix[dy][dx] == 1:
                    homes += 1

    cost = -(K**2 + (K-1)**2)
    cost += homes * M

    if new_q:
        searching(K, visited, cost, new_q, homes)
    else:
        if cost >= 0 and ans < homes:
            ans = homes
        return


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        for j in range(N):
            visited = [[0] * N for _ in range(N)]
            visited[i][j] = 1
            q = deque()
            q.append((i, j))
            # print(i, j)
            if matrix[i][j] == 1:
                searching(1, visited, M-1, q, 1)
            else:
                searching(1, visited, -1, q, 0)

    print(f'#{tc} {ans}')

