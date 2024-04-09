import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    list_ = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0
    cnt = 0

    for i in range(N):
        for j in range(N):
            temp = list_[i][j]
            for x in range(i, N):
                for y in range(j, N):
                    if temp == list_[x][y]:
                        width = x-i+1
                        height = y-j+1
                        area = width * height
                        if max_ < area:
                            max_ = area
                            cnt = 1
                        elif max_ == area:
                            cnt += 1

    print(f'#{tc} {cnt}')