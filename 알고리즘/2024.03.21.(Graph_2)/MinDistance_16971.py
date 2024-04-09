import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    lines = [list(map(int, input().split())) for _ in range(E)]
    ways = [float('inf')] * (N+1)
    ways[0] = 0

    for i in range(E):
        s, e, d = lines[i]
        if s == 0 or ways[s] != float('inf'):
            ways[e] = min(ways[e], ways[s] + d)

    print(f'#{tc} {ways[N]}')
