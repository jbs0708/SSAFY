import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

xi = [1, 0, 1, -1]
yi = [0, 1, 1, 1]

def check(y,x):
    for d in range(4):
        cnt = 0
        dx = x
        dy = y
        for _ in range(5):
            if 0 <= dx < N and 0 <= dy < N and matrix[dy][dx] == 'o':
                cnt += 1
                if cnt == 5:
                    return True
                dx += xi[d]
                dy += yi[d]
            else:
                break


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]

    found = False
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'o':
                if check(i, j):
                    print(f'#{tc} YES')
                    found = True
                    break
        if found:
            break
    if not found:
        print(f'#{tc} NO')
