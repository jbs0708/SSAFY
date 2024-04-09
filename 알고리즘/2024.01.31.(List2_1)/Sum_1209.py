import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = 10
N = 100

for tc in range(1, T+1):
    n = input()
    row = [0] * 100
    col = [0] * 100
    lc = 0
    rc = 0

    for r in range(N):
        temp = list(map(int, input().split()))
        for c in range(N):
            row[r] += temp[c]
            col[c] += temp[c]
            if r == c:
                rc += temp[c]
            if (r + c) == (N-1):
                lc += temp[c]

    max_ = max(max(row), max(col), lc, rc)
    print(f'#{tc} {max_}')


