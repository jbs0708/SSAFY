import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def dfs(visited, sum_, idx):
    global ans

    if sum_ >= B:
        if sum_ == B:
            ans = 0
            return
        else:
            ans = min(ans, sum_-B)

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = 1
            dfs(visited, sum_ + cl[i], i)
            visited[i] = 0



T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    cl = list(map(int, input().split()))
    visited = [0] * N
    ans = float('inf')

    dfs(visited, 0, 0)

    print(f'#{tc} {ans}')