import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    ans_list = [[''] * N for _ in range(N)]

    # 90
    for i in range(N):
        for j in range(N-1, -1, -1):
            ans_list[i][0] += str(num_list[j][i])

    # 180
    x = 0
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            ans_list[x][1] += str(num_list[i][j])
        x += 1

    # 270
    x = 0
    for i in range(N-1, -1, -1):
        for j in range(N):
            ans_list[x][2] += str(num_list[j][i])
        x += 1

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(f'{ans_list[i][j]}',end=' ')
        print()