import sys
import itertools

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    list_ = list(map(int, input().split()))
    ans = 0

    for i in range(1, min(N+1, K+1)):
        temp = list(itertools.combinations(list_, i))

        for t in temp:
            if sum(t) == K:
                ans += 1

    print(f'#{tc} {ans}')

