import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = 10

for tc in range(1, T + 1):
    L, S = map(int, input().split())
    visited = [0] * 101
    graph = [[] for _ in range(101)]
    data = list(map(int, input().split()))

    for i in range(0, L, 2):
        graph[data[i]].append(data[i+1])

    q = deque()
    q.append(graph[S])

    v = 0
    max_ = -1
    v_max = 0
    while q:
        v += 1
        q_list = q.popleft()
        temp = []
        for i in q_list:
            if visited[i] == 0:
                if v_max < v:
                    max_ = 0
                    v_max = v
                visited[i] = v
                max_ = max(max_, i)
                temp += graph[i]
        if temp:
            q.append(temp)

    print(f'#{tc} {max_}')




