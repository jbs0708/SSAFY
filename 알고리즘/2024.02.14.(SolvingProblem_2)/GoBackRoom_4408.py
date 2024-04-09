import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    aisle = [0] * 200
    for i in range(N):
        s, e = map(int, input().split())
        s, e = (s-1)//2, (e-1)//2
        if s > e:
            s, e = e, s
        for idx in range(s, e+1):
            aisle[idx] = aisle[idx] + 1

    print(f'#{tc} {max(aisle)}')

