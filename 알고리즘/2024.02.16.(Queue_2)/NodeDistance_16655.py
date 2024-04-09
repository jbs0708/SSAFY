import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    visited = [0] * (V+1)
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    S, G = map(int, input().split())
    q = deque()
    q.append(graph[S])

    v = 0
    found = False
    max_ = 0
    while q:
        v += 1
        q_list = q.popleft()
        temp = []
        for i in q_list:
            if visited[i] == 0:
                visited[i] = v
                if i == G:
                    max_ = v
                    found = True
                    break
                temp += graph[i]
        if temp:
            q.append(temp)
        if found:
            break

    print(f'#{tc} {max_}')



