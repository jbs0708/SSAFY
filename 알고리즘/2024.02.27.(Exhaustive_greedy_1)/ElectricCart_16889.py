import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def func(cnt, temp, x):
    global min_

    if cnt == N-1:
        if temp + list_[x][0] < min_:
            min_ = temp + list_[x][0]
        return

    for i in range(1, N):
        if list_[x][i] + temp < min_ and visited[i] == 0 and list_[x][i] != 0:
            visited[i] = 1
            temp += list_[x][i]
            func((cnt + 1), temp, i)
            visited[i] = 0
            temp -= list_[x][i]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    min_ = float('inf')
    list_ = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    func(0, 0, 0)

    print(f'#{tc} {min_}')

