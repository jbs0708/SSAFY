import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    carrot_list = list(map(int, input().split()))

    max_ = 1
    cnt = 1
    for n in range(1, N):
        if carrot_list[n-1] < carrot_list[n]:
            cnt += 1
            max_ = max(max_, cnt)
        else:
            cnt = 1

    print(f'#{tc} {max_}')