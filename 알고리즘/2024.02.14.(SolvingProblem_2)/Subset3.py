def f(i, k, s, t):
    global N
    if s == t:
        cnt = 0
        for j in range(k):
            if bit[j]:
                cnt += 1
                print(A[j], end=' ')
        print()
        if N == cnt:
            return True
    elif i == k:
        return
    elif s > t:
        return
    else:
        # 갈림길 1
        bit[i] = 1
        f(i+1, k, s+A[i], t)
        # 갈림길 2
        bit[i] = 0
        f(i+1, k, s, t)


T = int(input())

for tc in range(1, T+1):
    N = 3
    size = 12
    K = 6
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    bit = [0] * size


    print(f'#{tc} {f(0, size, 0, K) + 0}')