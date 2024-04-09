import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T + 1):
    NQ = list(map(int, input().split()))
    N = NQ[0]
    Q = NQ[1]
    n_list = [0] * N

    for i in range(1, Q+1):
        LR = list(map(int, input().split()))
        L = LR[0]
        R = LR[1]
        for loc in range(L-1, R):
            n_list[loc] = i


    print(f'#{tc} ',end='')
    for i in range(N):
        print(n_list[i],end=' ')
    print()