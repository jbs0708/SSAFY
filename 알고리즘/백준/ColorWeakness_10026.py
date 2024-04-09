import sys

limit_number = 15000
sys.setrecursionlimit(limit_number)

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def search_all(y, x, c):
    for i in range(4):
        dx = x + xi[i]
        dy = y + yi[i]

        if 0 <= dx < N and 0 <= dy < N and visit_all[dy][dx] == 0:
            color = list_[dy][dx]
            if c == color:
                visit_all[dy][dx] = 1
                search_all(dy, dx, c)
    return

def search_rg(y, x, c):
    for i in range(4):
        dx = x + xi[i]
        dy = y + yi[i]

        if 0 <= dx < N and 0 <= dy < N and visit_rg[dy][dx] == 0:
            color = list_[dy][dx]
            if c == 'R' or c == 'G':
                if color == 'G' or color == 'R':
                    visit_rg[dy][dx] = 1
                    search_rg(dy, dx, c)
            elif c == 'B' and color == 'B':
                visit_rg[dy][dx] = 1
                search_rg(dy, dx, c)
    return


N = int(input())
list_ = [list(input()) for _ in range(N)]

cnt_all = 0
cnt_rg = 0

visit_all = [[0] * N for _ in range(N)]
visit_rg = [[0] * N for _ in range(N)]

xi = [0, 0, 1, -1]
yi = [1, -1, 0, 0]

for y in range(N):
    for x in range(N):
        if visit_all[y][x] == 0:
            visit_all[y][x] = 1
            search_all(y, x, list_[y][x])
            cnt_all += 1

        if visit_rg[y][x] == 0:
            visit_rg[y][x] = 1
            search_rg(y, x, list_[y][x])
            cnt_rg += 1

print(f'{cnt_all} {cnt_rg}')

