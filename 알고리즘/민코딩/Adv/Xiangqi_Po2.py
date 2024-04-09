import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


xi = [0, 0, 1, -1]
yi = [1, -1, 0, 0]


def goable(x, y, field, depth):
    if depth < 3:
        for d in range(4):
            dx = x
            dy = y
            jump = False
            while True:
                dx = dx + xi[d]
                dy = dy + yi[d]
                if 0 <= dx < N and 0 <= dy < N:
                    if field[dx][dy] == 1:
                        if not jump:
                            jump = not jump
                        else:
                            goable_pos_lst.append([dx, dy])
                            if not [dx, dy] in eatable_private:
                                eatable_private.append([dx, dy])
                            field[dx][dy] = 0
                            goable(dx, dy, field, depth + 1)
                            field[dx][dy] = 1
                            break
                    elif field[dx][dy] == 0 and jump:
                        goable_pos_lst.append([dx, dy])
                        goable(dx, dy, field, depth+1)

                else:
                    break


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    y, x = -1, -1
    for i in range(N):
        for j in range(N):
            if matrix[x][y] == 2:
                y = i
                x = j
                matrix[x][y]= 0
                break

    goable_pos_lst = [[x, y]]
    eatable_private = []
    goable(x, y, matrix, 0)

    print(f'#{tc} {len(eatable_private)}')
