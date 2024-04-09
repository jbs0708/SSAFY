import sys
import math

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input()) + 1

    list_ = [list(map(int, input().split())) for _ in range(N)]
    x, y = -1, -1
    list_1 = []

    for i in range(N):
        for j in range(N):
            if list_[i][j] == 2:
                x = i
                y = j
            elif list_[i][j] == 1:
                list_1.append((i, j))

    max_ = 0
    for i in range(len(list_1)):
        temp_x = abs(list_1[i][0] - x)
        temp_y = abs(list_1[i][1] - y)
        temp = (temp_x * temp_x) + (temp_y * temp_y)
        max_ = max(temp, max_)

    d = math.sqrt(max_)
    if d == int(d):
        print(f'#{tc} {int(d)}')
    else:
        max_ = int(d) + 1
        print(f'#{tc} {max_}')



