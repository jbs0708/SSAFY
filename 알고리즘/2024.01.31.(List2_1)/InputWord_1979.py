import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    NK = list(map(int, input().split()))
    N, K = NK[0], NK[1]

    list_ = [list(map(int, input().split())) for _ in range(N)]

    max_ = 0

    for i in range(N):
        cnt = 0
        max_ = 0
        for j in range(N):
            if list_[i][j] == 1:
                cnt += 1
                if max_ < cnt:
                    max_ = cnt
            else:
                if max_ == K:
                    max_ += 1
                max_ = 0
                cnt = 0
        if max_ == K:
            max_ += 1

    for i in range(N):
        cnt = 0
        max_ = 0
        for j in range(N):
            if list_[j][i] == 1:
                cnt += 1
                if max_ < cnt:
                    max_ = cnt
            else:
                if max_ == K:
                    max_ += 1
                max_ = 0
                cnt = 0
        if max_ == K:
            max_ += 1

    print(f'#{tc} {max_}')
