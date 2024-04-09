import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    n_list = []
    for n in range(N):
        temp_list = list(map(int, input().split()))
        n_list.append(temp_list)
    P = int(input())
    ans_list = [0] * P

    for i in range(P):
        p = int(input())
        for n in range(N):
            if n_list[n][0] <= p <= n_list[n][1]:
                ans_list[i] += 1

    print(f'#{tc} ',end='')
    for a in ans_list:
        print(f'{a} ', end='')
    print()
