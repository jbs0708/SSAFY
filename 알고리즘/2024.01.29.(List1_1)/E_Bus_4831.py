import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T+1):
    KNM = list(map(int, input().split()))
    K = KNM[0]
    N = KNM[1]
    M = KNM[2]

    m_list = list(map(int, input().split()))

    pointer = 0
    cnt = 0

    while pointer + K < N:
        for i in range(K, 0, -1):
            if pointer + i in m_list:
                pointer += i
                cnt += 1
                break
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')