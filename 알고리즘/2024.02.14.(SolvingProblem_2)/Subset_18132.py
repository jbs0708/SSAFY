import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def f(i, k, s, t):
    global N
    global max_
    if s == t:
        cnt = 0
        for j in range(k):
            if bit[j]:
                cnt += 1
        if N == cnt:
            ans += 1
            return
    elif i == k:
        return
    elif s > t:
        return
    else:
        # 갈림길 1
        bit[i] = 1
        f(i + 1, k, s + A[i], t)
        # 갈림길 2
        bit[i] = 0
        f(i + 1, k, s, t)


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    size = 12
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    bit = [0] * size
    max_ = 0
    f(0, size, 0, K)

    print(f'#{tc} {max_}')
