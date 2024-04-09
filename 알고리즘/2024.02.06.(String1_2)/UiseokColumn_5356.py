import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N = 5

    list_ = [list(input()) for _ in range(N)]
    max_ = 0

    for n in range(N):
        max_ = max(max_, len(list_[n]))

    print(f'#{tc} ',end='')
    for i in range(max_):
        for j in range(N):
            if i < len(list_[j]):
                print(list_[j][i], end='')
    print()
