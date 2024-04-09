import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def dfs(visited, graph, s):
    visited[s] = True

    for i in graph[s]:
        if not visited[i]:
            dfs(visited, graph, i)


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V + 1)

    for e in range(E):
        s, g = map(int, input().split())
        graph[s].append(g)

    s, e = map(int, input().split())

    dfs(visited, graph, s)

    print(f'#{tc} {(visited[s] and visited[e]) + 0}')
