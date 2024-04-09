import sys

sys.setrecursionlimit = (10**6)

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline


def StoT(node, route, max_node):
    print(node, route)
    route.add(node)

    if node == T:
        r_route = set()
        r_max_node = [0] * (n+1)
        TtoS(node, r_route, route, r_max_node)
    elif max_node[node] < len(route):
        max_node[node] = max_node[node] | route

        for nxt_n in graph[node]:
            StoT(nxt_n, route, max_node)


def TtoS(node, r_route, route, r_max_node):
    global ans
    print('TtoS', end='  ')
    print(node, r_route)
    r_route.add(node)

    if node == S:
        temp = len(r_route & route)
        ans = max(ans, temp)
        print(f'comp: {route}, {r_route}')
        print(f'temp: {temp}')
        return
    elif r_max_node[node] < len(r_route):
        r_max_node[node] = len(r_route)

        for nxt_n in graph[node]:
            TtoS(nxt_n, r_route, route, r_max_node)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
route = set()
ans = 0
max_node = [set()] * (n + 1)

for i in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)


S, T = map(int, input().split())

StoT(S, route, max_node)

ans = max(ans-2, 0)

print(ans)