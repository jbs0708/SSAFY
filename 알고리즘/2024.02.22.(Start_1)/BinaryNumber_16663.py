import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N, M = input().split()

    temp = '0x' + M
    deci = int(temp, 16)
    max_ = format(deci, 'b')

    while True:
        if len(max_) % 4 != 0:
            max_ = '0' + max_
        else:
            break

    print(f'#{tc} {max_}')
