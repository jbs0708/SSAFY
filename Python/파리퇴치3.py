def check(x, y, dx, dy):
    global mx
    sum = arr[x][y]
    for i in range(4):
        for j in range(1,M):
            nx = x + dx[i] * j
            ny = y + dy[i] * j

            if (nx < 0 or ny < 0 or nx >= N or ny >= N):
                continue
            else:
                sum += arr[nx][ny]
    
    if (mx < sum):
        mx = sum
    return

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dxp = [1, -1, 0, 0]
    dyp = [0, 0, 1, -1]
    dxm = [1, -1, 1, -1]
    dym = [1, -1, -1 ,1]
    mx = 0
    for i in range(N):
        for j in range(N):
            check(i, j, dxp, dyp)
            check(i, j, dxm, dym)
    print('#{} {}'.format(tc, mx))