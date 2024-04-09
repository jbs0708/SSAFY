import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    matrix = [[0] * 1000 for _ in range(1000)]
    max_ = 4

    temp1 = list(map(int, input().split()))
    r1, c1, r2, c2 = temp1[0], temp1[1], temp1[2], temp1[3]
    temp2 = list(map(int, input().split()))
    rr1, cc1, rr2, cc2 = temp2[0], temp2[1], temp2[2], temp2[3]

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            matrix[i][j] = 1

    for i in range(rr1+1, rr2):
        for j in range(cc1+1, cc2):
            if matrix[i][j] == 1:
                max_ = 1
                break
        if max_ == 1:
            break

    if max_ == 1:
        print(f'#{tc} {max_}')
    else:
        set_list = []
        set_list.append((r1, c1))
        set_list.append((r2, c2))
        set_list.append((rr1, cc1))
        set_list.append((rr2, cc2))

        for i in range(4):
            for j in range(4):
                if i != j:
                    if set_list[i] == set_list[j]:
                        max_ = 3
                        break
            if max_ == 3:
                break

        if max_ != 3 :
            for i in range(4):
                for j in range(4):
                    if i % 2 == j % 2:
                        if temp1[i] == temp2[j]:
                            max_ = 2
                            break
                if max_ == 2:
                    break
        print(f'#{tc} {max_}')