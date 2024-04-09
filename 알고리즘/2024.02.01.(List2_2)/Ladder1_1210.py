import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    snail_list = [[0] * N for _ in range(N)]

    xi = [1, 0, -1, 0]
    yi = [0, -1, 0, 1]

    cnt = 2
    x = 0
    y = 0
    snail_list[0][0] = 1
    while cnt <= N*N:
        for i in range(4):
            while True:
                dx = x + xi[i]
                dy = y + yi[i]
                if 0 <= dx < N and 0 <= dy < N and snail_list[dy][dx] == 0:
                    snail_list[dy][dx] = cnt
                    x = dx
                    y = dy
                    cnt += 1
                else:
                    break

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(f'{snail_list[i][j]}', end=' ')
        print()
