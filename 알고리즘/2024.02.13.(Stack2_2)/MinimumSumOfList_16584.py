import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def func(x, visited, temp):
    global min_

    if x == N:
        if temp < min_:
            min_ = temp
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            temp += list_[x][i]
            func((x+1), visited, temp)
            visited[i] = 0
            temp -= list_[x][i]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = [[] for _ in range(10)]
    min_ = 500
    list_ = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        visited = [0] * N
        visited[i] = 1
        temp = list_[0][i]
        func(1, visited, temp)

    print(f'#{tc} {min_}')