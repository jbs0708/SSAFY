import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T + 1):
    DABF = list(map(int, input().split()))

    D = DABF[0]
    A = DABF[1]
    B = DABF[2]
    F = DABF[3]

    max_ = 0
    time = D / (A+B)
    max_ += F * time

    print(f'#{tc} {max_}')




