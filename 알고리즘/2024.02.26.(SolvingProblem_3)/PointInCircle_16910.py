import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    max_ = 0

    for i in range(N+1):
        for j in range(1, N+1):
            if i**2 + j**2 <= N**2:
                max_ += 1

    max_ *= 4
    max_ += 1

    print(f'#{tc} {max_}')
