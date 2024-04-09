import sys
import heapq

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

xi = [0, 0, 1, -1]
yi = [1, -1, 0, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    min_cost = [[float('inf')] * N for _ in range(N)]
    min_cost[0][0] = 0

    h = [(0, 0, 0)]

    while h:
        t, y, x = heapq.heappop(h)

        if y == N-1 and x == N-1:
            break

        for d in range(4):
            dx = x + xi[d]
            dy = y + yi[d]

            if 0 <= dx < N and 0 <= dy < N:
                t += matrix[dy][dx]

                if min_cost[dy][dx] > t:
                    min_cost[dy][dx] = t
                    heapq.heappush(h, (t, dy, dx))

                t -= matrix[dy][dx]

    print(f'#{tc} {min_cost[N-1][N-1]}')
