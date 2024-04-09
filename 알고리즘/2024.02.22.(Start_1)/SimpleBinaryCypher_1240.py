import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    line = []
    for i in range(N):
        if matrix[i].count('1'):
            line = matrix[i]

    idx = -1
    for i in range(M-1, -1, -1):
        if line[i] == '1':
            idx = i
            break

    line = line[idx-55:idx+1]
    cypher = []
    for i in range(0, len(line), 7):
        temp = line[i:i+7]
        cypher.append(temp)

    rule = [[3,2,1,1], [2,2,2,1], [2,1,2,2], [1,4,1,1], [1,1,3,2], [1,2,3,1], [1,1,1,4], [1,3,1,2], [1,2,1,3], [3,1,1,2]]
    password = []
    sum_password = 0
    for i in range(8):
        num_check = []
        cnt = 0
        for j in range(7):
            if j == 0:
                cnt += 1
            else:
                if cypher[i][j] == cypher[i][j-1]:
                    cnt += 1
                else:
                    num_check.append(cnt)
                    cnt = 1
        num_check.append(cnt)

        for r in range(10):
            if rule[r] == num_check:
                sum_password += r
                password.append(r)
                break

    sum_ = 0
    for p in range(8):
        if p % 2 == 1:
            sum_ += password[p]
        else:
            sum_ += password[p]*3

    if sum_ % 10 == 0:
        print(f'#{tc} {sum_password}')
    else:
        print(f'#{tc} 0')