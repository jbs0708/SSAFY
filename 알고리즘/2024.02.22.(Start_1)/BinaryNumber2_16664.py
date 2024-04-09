import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N = float(input())

    max_ = ''
    i = -1
    while N > 0:
        temp = 2**i
        if N - temp >= 0:
            N -= temp
            max_ += '1'
        else:
            max_ += '0'

        i -= 1

        if len(max_) > 12:
            max_ = 'overflow'
            break

    print(f'#{tc} {max_}')
