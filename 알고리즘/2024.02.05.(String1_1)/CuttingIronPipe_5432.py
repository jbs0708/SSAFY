import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    parenthesis_list = list(input())

    max_ = 0
    cnt = 0
    p = 0
    while p < len(parenthesis_list):
        if parenthesis_list[p] == '(':
            cnt += 1
        elif parenthesis_list[p] == ')':
            if parenthesis_list[p-1] == '(':
                cnt -= 1
                max_ += cnt
            else:
                cnt -= 1
                max_ += 1

        p += 1

    print(f'#{tc} {max_}')




