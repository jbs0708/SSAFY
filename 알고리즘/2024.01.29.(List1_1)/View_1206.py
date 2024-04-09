import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))
    sum_ = 0

    for n in range(2, N - 2):
        if buildings[n] <= buildings[n + 1] or buildings[n] <= buildings[n + 2]:
            if buildings[n + 1] <= buildings[n + 2]:
                n += 2
                continue
            else:
                n += 1
                continue

        if buildings[n] <= buildings[n-2] or buildings[n] <= buildings[n-1]:
            n += 3
            continue

        if buildings[n] > buildings[n+1] and buildings[n] > buildings[n+1]:
            temp = max(buildings[n - 1],buildings[n - 2],buildings[n + 1],buildings[n + 2])
            sum_ += buildings[n] - temp
            n += 3
            continue

    print(f'#{tc} {sum_} ')
