import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline

xi = [0, 0, 1, -1]
yi = [1, -1, 0, 0]


def func(cnt, visited, y, x):
    global ans

    if (y, x) in order:
        if cnt == order.index((y, x)):
            cnt += 1
        else:
            return

    if (y, x) == order[m - 2]:
        ans += 1
        return

    for d in range(4):
        dx = x + xi[d]
        dy = y + yi[d]

        if 0 <= dx < n and 0 <= dy < n and not visited[dy][dx] and not matrix[dy][dx]:
            visited[y][x] = 1
            func(cnt, visited, dy, dx)
            visited[y][x] = 0


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
order = []
ans = 0
for _ in range(m):
    r, c = map(int, input().split())
    order.append((r-1, c-1))

y, x = order.pop(0)
visited[y][x] = 1

func(0, visited, y, x)

print(ans)






