import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    list_ = list_ = list(map(int,(list(input()))))

    max_ = 0
    num = 0
    for n in range(10):
        if list_.count(n) >= max_:
            max_ = list_.count(n)
            num = n


    print(f'#{tc} {num} {max_}')