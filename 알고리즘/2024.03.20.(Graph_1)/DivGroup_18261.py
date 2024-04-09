import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def link_check(idx):
    if not visited[idx]:
        visited[idx] = 1

    for i in group[idx]:
        if not visited[i]:
            link_check(i)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    list_ = list(map(int, input().split()))
    visited = [0] * (N+1)
    group = [[] for _ in range(N+1)]
    ans = 0

    for i in range(0, M):
        a, b = list_[i*2], list_[i*2+1]
        group[a].append(b)
        group[b].append(a)

    for i in range(1, N+1):
        if not visited[i]:
            link_check(i)
            ans += 1

    print(f'#{tc} {ans}')
