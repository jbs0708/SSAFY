import sys
import heapq

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pos_x = list(map(int, input().split()))
    pos_y = list(map(int, input().split()))
    tax = float(input())

    # edge = [[] for _ in range(N)]
    # for i in range(N-1):
    #     for j in range(i+1, N):
    #         d = abs(pos_x[i] - pos_x[j])**2 + abs(pos_y[i] - pos_y[j])**2
    #         d *= tax
    #         edge[i].append([d, j])
    #         edge[j].append([d, i])

    visited = [False] * N
    h = [(0, 0)]
    ans = 0
    cnt = 0
    while h:
        d, v = heapq.heappop(h)
        if cnt == N+1:
            break
        if visited[v]:
            continue
        visited[v] = True
        ans += d
        cnt += 1
        for nv in range(N):
            if not visited[nv]:
                nd = abs(pos_x[nv] - pos_x[v])**2 + abs(pos_y[nv] - pos_y[v])**2
                heapq.heappush(h, (nd, nv))

    print(f'#{tc} {round(ans*tax)}')
