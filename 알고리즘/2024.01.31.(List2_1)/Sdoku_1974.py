import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    list_ = [list(map(int, input().split())) for _ in range(9)]

    found = True
    for i in range(9):
        check = [0] * 10
        for j in range(9):
            check[list_[i][j]] += 1
            if check[list_[i][j]] > 1:
                found = False
                break
        if not found:
            break

        check = [0] * 10
        for j in range(9):
            check[list_[j][i]] += 1
            if check[list_[j][i]] > 1:
                found = False
                break

    if found:
        loc = [0, 3, 6]
        for i in loc:
            for j in loc:
                check = [0] * 10
                for y in range(3):
                    for x in range(3):
                        check[list_[y][x]] += 1
                        if check[list_[y][x]] > 1:
                            found = False
                            break
                    if not found:
                        break
                if not found:
                    break
            if not found:
                break
    if found:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

