import sys
import heapq

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def dijkstra(s, graph):
    cost_list = [float('inf')] * (N+1)
    cost_list[s] = 0
    hq = [[0, s]]

    while hq:
        cost, node = heapq.heappop(hq)
        for nxt_c, nxt_n in graph[node]:
            if cost + nxt_c < cost_list[nxt_n]:
                cost_list[nxt_n] = cost + nxt_c
                heapq.heappush(hq, [cost_list[nxt_n], nxt_n])

    return cost_list


T = int(input())

for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    graph_X = [[] for _ in range(N+1)]
    graph_H = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    ans = 0

    for m in range(M):
        x, y, c = map(int, input().split())
        graph_X[x].append((c,y))
        graph_H[y].append((c,x))

    XtoH_list = dijkstra(X, graph_X)
    HtoX_list = dijkstra(X, graph_H)

    for node in range(1, N+1):
        ans = max(XtoH_list[node] + HtoX_list[node], ans)

    print(f'#{tc} {ans}')
