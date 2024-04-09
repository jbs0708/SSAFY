import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def dfs(s, graph, visited):
    visited[s] = True

    for i in graph[s]:
        if not visited[i]:
            dfs(i, graph, visited)


T = 10

for tc in range(1, T + 1):
    tc, size = map(int, input().split())
    visited = [False] * 100
    graph = [[] for _ in range(100)]

    route_list = list(map(int, input().split()))
    for i in range(0, size*2, 2):
        graph[route_list[i]].append(route_list[i+1])

    dfs(0, graph, visited)

    print(f'#{tc} {(visited[0] and visited[99]) + 0}')