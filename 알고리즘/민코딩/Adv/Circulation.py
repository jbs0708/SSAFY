import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nodes = list(map(int, input().split()))
    ans = 0

    for i in range(N):
        for j in range(i, N):
            # 안쪽
            for p in range(i, j):
                for q in range(p, j):
                    if abs(i-p) <= 1 or abs(i-q) <= 1 or abs(j-p) <= 1 or abs(j-q) <= 1 or abs(i-j) <= 1 or abs(p-q) <= 1 or j-i == N-1 or q - i == N-1:
                        continue
                    else:
                        x, y = nodes[i], nodes[j]
                        n, m = nodes[p], nodes[q]
                        l1 = (x + y)**2
                        l2 = (n + m)**2
                        ans = max(ans, l1 + l2)

            # 바깥쪽
            for p in range(j, N):
                for q in range(p, N):
                    if abs(i-p) <= 1 or abs(i-q) <= 1 or abs(j-p) <= 1 or abs(j-q) <= 1 or abs(i-j) <= 1 or abs(p-q) <= 1 or j-i == N-1 or q - i == N-1:
                        continue
                    else:
                        x, y = nodes[i], nodes[j]
                        n, m = nodes[p], nodes[q]
                        l1 = (x + y) ** 2
                        l2 = (n + m) ** 2
                        ans = max(ans, l1 + l2)

    print(f'#{tc} {ans}')
