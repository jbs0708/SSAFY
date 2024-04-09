import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N = input()
    M = input()
    len_N = len(N)
    len_M = len(M)

    found = False
    cnt = 0
    for m in range(len_M - len_N + 1):
        for n in range(len_N):
            if N[n] != M[n+m]:
                cnt = 0
                break
            else:
                cnt += 1
                if cnt == len_N:
                    found = True
                    break
        if found:
            break

    if found:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')