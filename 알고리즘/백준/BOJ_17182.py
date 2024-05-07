import sys

sys.stdin = open("input.txt")


N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * (N + 1)
visited[K] = 1
ans = float('inf')

# 플로이드-와샬
for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])


def func(cur, temp, cnt):
    global ans

    if N == cnt:
        ans = min(ans, temp)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            func(i, temp + matrix[cur][i], cnt+1)
            visited[i] = 0


func(K, 0, 1)
print(ans)
