import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N = NM[0]
    M = NM[1]
    list_ = list(map(int, input().split()))
    max_ = 0
    sum_list = []

    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += list_[i+j]
        sum_list.append(temp)

    max_ = max(sum_list) - min(sum_list)

    print(f'#{tc} {max_}')