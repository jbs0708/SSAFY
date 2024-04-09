import sys
import math

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n = (N // 10)
    max_ = 1
    quotient = n//2
    mod = n%2

    for i in range(quotient):
        all = math.factorial((quotient - i) + mod + (2 * i))
        num_big = math.factorial((quotient - i))
        num_small = math.factorial(mod + (2 * i))
        temp = num_big * num_small
        num = all / temp

        max_ += num * (2 ** (quotient - i))


    print(f'#{tc} {int(max_)}')

