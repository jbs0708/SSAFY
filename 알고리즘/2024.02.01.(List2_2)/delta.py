
def list_printer(cnt, input_list):
    print(f'## {cnt} ##')
    for i in range(N):
        for j in range(N):
            print(f'{input_list[i][j]}',end=' ')
        print()
    print()


N = 3

list_ = [[0] * N for _ in range(N)]

# direction(=delta)
xi = [1, 0, -1, 0]
yi = [0, -1, 0, 1]

# start_point
x = 0
y = 0
cnt = 1
list_[y][x] = cnt # 초기값 설정
list_printer(cnt, list_) # 출력

while cnt < N*N:
    # 방향키
    for i in range(4):
        while True:
            dx = x + xi[i]
            dy = y + yi[i]

            if 0 <= dx < N and 0 <= dy < N and list_[dy][dx] == 0:
                cnt += 1
                list_[dy][dx] = cnt
                # 현재위치 변경
                x = dx
                y = dy
                input() # 엔터쳐야 다음꺼 나오게
                list_printer(cnt, list_)
            else:
                break
