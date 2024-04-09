import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]

    ans_list = list(map(int, input().split()))
    list_ = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0
    min_ = 821


    for n in range(N):
        cnt = 1
        score = 0
        for m in range(M):
            if ans_list[m] == list_[n][m]:
                score = score + cnt
                cnt = cnt + 1
            else:
                cnt = 1
        max_ = max(score, max_)
        min_ = min(score, min_)

    max_ = max_ - min_

    print(f'#{tc} {max_}')
