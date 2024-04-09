import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def oprimal_route(pos, cur_dis, cnt):
    global max_
    if cur_dis > ans:
        return

    x, y = pos
    if cnt == N+1:
        nx, ny = home
        dis = abs(nx - x) + abs(ny - y)

        if ans > cur_dis + dis:
            ans = cur_dis + dis
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            nx, ny = customer[i]
            dis = abs(nx - x) + abs(ny - y)
            oprimal_route(customer[i], cur_dis + dis, cnt + 1)
            visited[i] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    min_ = float('inf')
    list_ = list(map(int, input().split()))
    company = (list_[0], list_[1])
    home = (list_[2], list_[3])
    customer = []
    max_ = float('inf')
    visited = [0] * (N+1)
    visited[0] = 1

    for i in range(4, 4+(N*2), 2):
        customer.append((list_[i], list_[i+1]))

    customer.insert(0, company)

    oprimal_route(company, 0, 1)

    print(f'#{tc} {max_}')

