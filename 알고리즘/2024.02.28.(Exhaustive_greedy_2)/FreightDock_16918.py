import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time_table = [tuple(map(int, input().split())) for _ in range(N)]
    time_table.sort(key = lambda x: x[1])
    ans = 0
    flag = -1

    for time in time_table:
        s, e = time
        if s >= flag:
            flag = e
            ans += 1

    print(f'#{tc} {ans}')

