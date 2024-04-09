def check(N):
    n = N
    arr = [0] * 10
    num = 0
    cnt = 1
    while True:
        while True:
            temp = n % 10
            if arr[temp] == 0:
                arr[temp] += 1
                num += 1
            if num == 10:
                break
            elif n > 9:
                n = n // 10
            else:
                break
        if num == 10:
            break
        else :
            cnt += 1
            n = cnt * N
    return cnt


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ans = check(N) * N
    print("#{} {}".format(tc, ans))
    