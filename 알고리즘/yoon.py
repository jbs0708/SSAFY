import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


code = {(2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4, (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7,
        (2, 1, 3): 8, (1, 1, 2): 9}

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    find_number = sorted(list(set(list(input().strip() for _ in range(N)))))[1:]
    number = 0
    visited = []

   ##############################################################################################################

    for i in range(len(find_number)):
        print(find_number[i])

        for num in find_number[i]:
            print(num)

        answer = ''.join([format(int('0x' + num, 16), '04b') for num in find_number[i]]).rstrip('0')
        print(answer)

    #############################################################################################################

        code_num = []
        n2, n3, n4 = 0, 0, 0

        for j in range(len(answer) - 1, -1, -1):
            if answer[j] == '1' and n3 == 0:
                n4 += 1
            elif answer[j] == '0' and n2 == 0:
                n3 += 1
            elif answer[j] == '1':
                n2 += 1
            elif answer[j] == '0':
                if answer[j - 1] == '1':

                    n = min(n2, n3, n4)
                    code_num.append(code[n2 // n, n3 // n, n4 // n])
                    n2, n3, n4 = 0, 0, 0
                    if len(code_num) == 8:
                        if ((code_num[1] + code_num[3] + code_num[5] + code_num[7]) * 3 + code_num[0] + code_num[2] +
                            code_num[4] + code_num[6]) % 10 == 0:
                            if code_num not in visited:
                                number += sum(code_num)
                                visited.append(code_num)
                        code_num = []

    print(f'#{test_case} {number}')