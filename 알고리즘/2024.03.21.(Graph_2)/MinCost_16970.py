import sys
import heapq

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

xi = [0, 0, 1, -1]
yi = [1, -1, 0, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_cost = [[float('inf')] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    min_cost[0][0] = 0

    h = []
    heapq.heappush(h, [0, 0, 0])

    while h:
        fuel, y, x = heapq.heappop(h)
        visited[y][x] = 1

        # if y == N-1 and x == N-1:
        #     break

        for d in range(4):
            dx = x + xi[d]
            dy = y + yi[d]

            if 0 <= dx < N and 0 <= dy < N and not visited[dy][dx]:
                after_fuel = fuel + 1
                if matrix[y][x] < matrix[dy][dx]:
                    after_fuel += matrix[dy][dx] - matrix[y][x]

                if min_cost[dy][dx] > after_fuel:
                    min_cost[dy][dx] = after_fuel
                    heapq.heappush(h, [after_fuel, dy, dx])

    print(f'#{tc} {min_cost[N-1][N-1]}')
