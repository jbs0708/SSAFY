import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    NK = list(map(int, input().split(', ')))
    N = NK[0]
    K = NK[1]

    list_ = list(map(int, input().split()))

    max_ = 0
    for i in range(1 << len(list_)):
        temp = 0
        cnt = 0
        for j in range(len(list_)):
            if i & (1 << j):
                cnt += 1
                temp += list_[j]
        if cnt == N:
            if temp == K:
                max_ += 1

    print(f'#{tc} {max_}')

