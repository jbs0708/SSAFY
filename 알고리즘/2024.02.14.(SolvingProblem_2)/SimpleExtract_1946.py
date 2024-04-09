import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    print(f'#{tc}')
    N = int(input())
    max_ = ''

    for i in range(N):
        s, n = input().split()
        num = int(n)
        for _ in range(num):
            max_ += s

    jump = 0
    for a in max_:
        print(a,end='')
        jump += 1
        if jump == 10:
            print()
            jump = 0
    print()
