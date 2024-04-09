import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    NK = list(map(int, input().split()))
    N = NK[0]
    K = NK[1]

    sample = list(map(int, input().split()))
    passCode = list(map(int, input().split()))

    cnt = 0
    loc = 0
    for i in range(K):
        p = passCode[i]
        for j in range(loc, N):
            s = sample[j]
            if p == s:
                cnt += 1
                loc = j+1
                break

    if cnt == K:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
