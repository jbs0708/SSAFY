import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    fuel_matrix = [[float('inf')] * N for _ in range(N)]
    fuel_matrix[0][0] = 0
    tunnel_fuel = []
    tunnel_list = []

    for m in range(M):
        temp = list(map(int, input().split()))
        point_1 = (temp[0]-1, temp[1]-1)
        point_2 = (temp[2]-1, temp[3]-1)
        fuel = temp[4]
        tunnel_list.append(point_1)
        tunnel_list.append(point_2)
        tunnel_fuel.append(fuel)

    q = deque()
    q.append([(0, 0), 0])

    # if (0, 0) in tunnel_list:
    #     idx = tunnel_list.index((0, 0))
    #     if idx % 2 == 0:
    #         end_point = tunnel_list[idx + 1]
    #     else:
    #         end_point = tunnel_list[idx - 1]
    #     fuel_matrix[end_point[0]][end_point[1]] = tunnel_fuel[idx//2]
    #     q.append([end_point, tunnel_fuel[idx//2]])


    xi = [0, 0, -1, 1]
    yi = [1, -1, 0, 0]

    while q:
        curr_point, curr_fuel_ = q.popleft()

        # print(curr_point)
        # for i in range(N):
        #     for j in range(N):
        #         print(fuel_matrix[i][j], end=' ')
        #     print()

        for d in range(4):
            curr_fuel = curr_fuel_
            t_fuel = curr_fuel_
            dx = curr_point[1] + xi[d]
            dy = curr_point[0] + yi[d]
            next_point = (dy, dx)

            if 0 <= dx < N and 0 <= dy < N:
                if curr_fuel >= fuel_matrix[dy][dx]:
                    continue

                if matrix[curr_point[0]][curr_point[1]] == matrix[next_point[0]][next_point[1]]:
                    curr_fuel += 1
                elif matrix[curr_point[0]][curr_point[1]] < matrix[next_point[0]][next_point[1]]:
                    diff = matrix[next_point[0]][next_point[1]] - matrix[curr_point[0]][curr_point[1]]
                    curr_fuel += diff * 2
                    # if curr_point == (1, 1) and next_point == (1, 2):
                    #     print(diff, curr_fuel)

                if fuel_matrix[next_point[0]][next_point[1]] >= curr_fuel:
                    fuel_matrix[next_point[0]][next_point[1]] = curr_fuel
                    if next_point != (N-1, N-1):
                        q.append([next_point, curr_fuel])

                temp_point = []
                temp_fuel = []
                while next_point in tunnel_list:
                    if next_point in tunnel_list:
                        idx = tunnel_list.index(next_point)
                        tunnel_end = tuple()
                        if idx % 2 == 0:
                            tunnel_end = tunnel_list[idx + 1]
                            temp_point.append(tunnel_list.pop(idx))
                            temp_point.append(tunnel_list.pop(idx))
                        else:
                            tunnel_end = tunnel_list[idx - 1]
                            temp_point.append(tunnel_list.pop(idx - 1))
                            temp_point.append(tunnel_list.pop(idx - 1))
                        add_fuel = tunnel_fuel[idx // 2]
                        temp_fuel.append(tunnel_fuel.pop(idx // 2))
                        t_fuel += add_fuel
                        # print()
                        if fuel_matrix[tunnel_end[0]][tunnel_end[1]] > t_fuel:
                            fuel_matrix[tunnel_end[0]][tunnel_end[1]] = t_fuel
                            q.append([tunnel_end, t_fuel])
                            # print(f'----- tunnel -----')
                            # print(curr_point, tunnel_end, curr_fuel)
                            # print()
                tunnel_list += temp_point
                tunnel_fuel += temp_fuel

    # for i in range(N):
    #     for j in range(N):
    #         print(fuel_matrix[i][j], end=' ')
    #     print()

    print(f'#{tc} {fuel_matrix[N-1][N-1]}')

