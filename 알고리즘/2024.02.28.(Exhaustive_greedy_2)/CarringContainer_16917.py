import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    containers = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    ans = 0

    flag = 0
    for t in trucks:
        for c in range(flag, N):
            if t >= containers[c]:
                ans += containers[c]
                flag = c + 1
                break

    print(f'#{tc} {ans}')

