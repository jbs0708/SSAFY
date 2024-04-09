def check(x, y, N, arr):
    global cnt
    # 끝에 도달하면 카운트
    if x == N-1 & y == N-1:
        cnt += 1
    # 3방향 전진
    if x+1 < N & arr[x+1][y] == 0:
        check(x+1,y,N,arr)
    if y+1 < N & arr[x][y+1] == 0:
        check(x,y+1,N,arr)
    if y+1 < N & x+1 < N & arr[x+1][y+1] == 0:
        check(x+1,y+1,N,arr)

    return


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

check(0,1,N,arr)
print(cnt)
