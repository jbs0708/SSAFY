import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def team(p):
    global visited

    visited[p] = 1
    for i in graph[p]:
        if not visited[i]:
            team(i)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    ans = 0

    for m in range(M):
        p1, p2 = map(int, input().split())
        graph[p1].append(p2)
        graph[p2].append(p1)

    for n in range(1, N+1):
        if not visited[n]:
            ans += 1
            team(n)

    print(f'#{tc} {ans}')
