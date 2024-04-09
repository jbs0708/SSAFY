import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def boom(x,y):
    cnt = -list_[x][y]

    for dx in range(x-P,x+P+1):
        if 0 <= dx < N:
            cnt += list_[dx][y]
    for dy in range(y-P, y+P+1):
        if 0 <= dy < N:
            cnt += list_[x][dy]

    return cnt


T = int(input())

for tc in range(1, T+1):
    NP = list(map(int, input().split()))
    N = NP[0]
    P = NP[1]

    list_ = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0

    for i in range(N):
        for j in range(N):
            max_ = max(boom(i,j), max_)

    print(f'#{tc} {max_}')