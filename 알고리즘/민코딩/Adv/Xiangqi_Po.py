import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def printer(dy, dx):
    global max_
    temp = matrix[dy][dx]
    matrix[dy][dx] = 7
    print(f'num: {ans}')
    print((dy, dx))
    for row in range(N):
        for col in range(N):
            print(matrix[row][col], end=' ')
        print()
    print()
    matrix[dy][dx] = temp
    return


def func(y, x, cnt, visited, jump, cont, matrix1):
    cnt += 1
    if cnt > 3:
        return
    else:
        for d in range(4):
            dx = x + xi[d]
            dy = y + yi[d]

            while 0 <= dx < N and 0 <= dy < N:
                if matrix1[dy][dx] == 1 and jump[d] == 0:
                    jump = [0, 0, 0, 0]
                    jump[d] = 1
                    cont = True
                elif matrix1[dy][dx] == 1 and jump[d] == 1:
                    if not visited[dy][dx] and not cont:
                        cont = True
                        jump = [0, 0, 0, 0]
                        jump[d] = 1
                        ny, nx = dy + yi[d], dx + xi[d]
                        func(ny, nx, cnt, visited, jump, cont, matrix1)

                        jump = [0, 0, 0, 0]
                        # print(f'ans: {dy, dx, cnt}')
                        visited[dy][dx] = True
                        matrix1[dy][dx] = 0
                        func(dy, dx, cnt, visited, jump, cont, matrix1)
                        matrix1[dy][dx] = 1

                        cont = False

                    elif not visited[dy][dx] and cont:
                        jump = [0, 0, 0, 0]
                        visited[dy][dx] = True
                        matrix1[dy][dx] = 0
                        cont = False
                        func(dy, dx, cnt, visited, jump, cont, matrix1)
                        matrix1[dy][dx] = 1

                    elif cont:
                        return

                    else:
                        jump = [0, 0, 0, 0]
                        matrix1[dy][dx] = 0
                        func(dy, dx, cnt, visited, jump, cont, matrix1)
                        matrix1[dy][dx] = 1
                        cont = False

                elif matrix1[dy][dx] == 0 and jump[d] == 1:
                    jump = [0, 0, 0, 0]
                    jump[d] = 1
                    func(dy, dx, cnt, visited, jump, cont, matrix1)
                    cont = False

                if matrix1[dy][dx] == 0:
                    cont = False

                dx += xi[d]
                dy += yi[d]


T = int(input())

xi = [0, 1, 0, -1]
yi = [-1, 0, 1, 0]

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0
    visited = [[False] * N for _ in range(N)]

    # for i in range(N):
    #     for j in range(N):
    #         print(matrix[i][j], end=' ')
    #     print()

    y, x = -1, -1
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                y = i
                x = j
    matrix[y][x] = 0
    visited[y][x] = True
    jump = [0, 0, 0, 0]
    func(y, x, 0, visited, jump, False, matrix)

    max_ = -1
    for i in range(N):
        max_ += visited[i].count(True)

    print(f'#{tc} {max_}')



