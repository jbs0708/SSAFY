import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = set(input().strip() for _ in range(N))
    visited = []
    real_sum = 0

    rule = [[2, 1, 1], [2, 2, 1], [1, 2, 2], [4, 1, 1], [1, 3, 2], [2, 3, 1], [1, 1, 4], [3, 1, 2], [2, 1, 3],
            [1, 1, 2]]

    for line in matrix:
        h_code = '0x' + line
        temp = int(h_code, 16)
        bin_ = format(temp, '04b')

        num_check = []
        sum_password = 0
        password = []
        sum_ = 0

        r1, r2, r3 = 0, 0, 0
        for i in range(len(bin_)-1, -1, -1):
            if bin_[i] == '1' and r2 == 0:
                r3 += 1
            elif bin_[i] == '0' and r1 == 0:
                r2 += 1
            elif bin_[i] == '1':
                r1 += 1
            elif bin_[i] == '0':
                # why?
                if bin_[i - 1] == '1':

                    rate = min(r1, r2, r3)
                    num_check.append(r1 // rate)
                    num_check.append(r2 // rate)
                    num_check.append(r3 // rate)

                    for r in range(10):
                        if rule[r] == num_check:
                            sum_password += r
                            password.append(r)

                    r1, r2, r3 = 0, 0, 0

                    if len(num_check) == 8:
                        for pw in range(8):
                            if pw % 2 == 1:
                                sum_ += password[pw]
                            else:
                                sum_ += password[pw] * 3

                    if sum_ % 10 == 0:
                        if num_check not in visited:
                            real_sum += sum_password
                            visited.append(num_check)

                    num_check = []
                    sum_ = 0
                    password = []
                    sum_password = 0

    print(f'#{tc} {real_sum}')
