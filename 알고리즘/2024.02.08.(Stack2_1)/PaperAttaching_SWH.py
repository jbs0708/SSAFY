import sys
sys.stdin = open("input.txt", "r")

t = int(input())

dp = [0 for _ in range(31)]
dp[1] = 1

for i in range(2, 31):
    if i % 2 == 0:
        dp[i] = 2 * dp[i - 1] + 1
    else:
        dp[i] = 2 * dp[i - 1] - 1

for tc in range(t):
    n = int(input()) // 10
    print(f"#{tc + 1} {dp[n]}")