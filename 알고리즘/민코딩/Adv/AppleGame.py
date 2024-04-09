import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    list_ = [list(map(int, input().split())) for _ in range(N)]
    seq_list = []

    num = 1
    # 리스트 전체의 최대값
    max_ = max(map(max, list_))

    while num <= max_:
        for y in range(N):
            for x in range(N):
                if list_[y][x] == num:
                    # 1부터 최대값까지 각 사과의 좌표 구하기
                    seq_list.append((y, x))
                    num += 1
                    if num > max_:
                        break
            if num > max_:
                break

    x, y = 0, 0
    # 4방향 표시 {0 : 동, 1: 남, 2 : 서, 3 : 북}
    dir_ = 0
    # 오른쪽으로 꺾은 횟수
    cnt = 0
    
    # 좌표를 순회하며, 현위치와 현방향을 기준으로
    # 다음 사과의 위치를 4분할해서 각 케이스 별로 꺾은 횟수와
    # 도착 후 방향을 설정한다
    for i in range(max_):
        dy = seq_list[i][0]
        dx = seq_list[i][1]

        # 동남
        if x < dx and y < dy:
            if dir_ == 0:
                cnt += 1
                dir_ = 1
            elif dir_ == 1:
                cnt += 3
                dir_ = 0
            elif dir_ == 2:
                cnt += 3
                dir_ = 1
            elif dir_ == 3:
                cnt += 2
                dir_ = 1

        # 서남
        elif x > dx and y < dy:
            if dir_ == 0:
                cnt += 2
                dir_ = 2
            elif dir_ == 1:
                cnt += 1
                dir_ = 2
            elif dir_ == 2:
                cnt += 3
                dir_ = 1
            elif dir_ == 3:
                cnt += 3
                dir_ = 2

        # 서북
        elif x > dx and y > dy:
            if dir_ == 0:
                cnt += 3
                dir_ = 3
            elif dir_ == 1:
                cnt += 2
                dir_ = 3
            elif dir_ == 2:
                cnt += 1
                dir_ = 3
            elif dir_ == 3:
                cnt += 3
                dir_ = 2

        # 동북
        elif x < dx and y > dy:
            if dir_ == 0:
                cnt += 3
                dir_ = 3
            elif dir_ == 1:
                cnt += 3
                dir_ = 0
            elif dir_ == 2:
                cnt += 2
                dir_ = 0
            elif dir_ == 3:
                cnt += 1
                dir_ = 0

        x, y = dx, dy

    print(f'#{tc} {cnt}')
