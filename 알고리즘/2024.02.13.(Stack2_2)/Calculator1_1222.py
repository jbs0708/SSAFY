import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    input_list = input()
    stack = ''
    max_ = ''
    sum_ = 0

    for i in range(N):
        if input_list[i].isnumeric():
            max_ += input_list[i]
            sum_ += int(input_list[i])
        else:
            stack += input_list[i]

    print(f'#{tc} {sum_}')
    # print(ans + stack)