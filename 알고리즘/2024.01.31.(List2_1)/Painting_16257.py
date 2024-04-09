import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    list_ = [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0

    for n in range(N):
        temp = list(map(int, input().split()))
        r1, c1, r2, c2 = temp[0], temp[1], temp[2], temp[3]
        color = temp[4]

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if list_[r][c] == 0:
                    list_[r][c] = color
                else:
                    list_[r][c] = 3
                    cnt += 1

    print(f'#{tc} {cnt}')