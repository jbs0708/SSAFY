import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

'''
1. 주사위는 북남으로 움직일 때 4개의 면이 위아래로 회전한다.
2. 동쪽으로 움직이면 오른쪽 면이 바닥, 왼쪽면이 하늘을 향한다.
3. 서쪽으로 움직이면 왼쪽 면이 바닥, 오른쪽면이 하늘을 향한다.
4. 이러한 원리를 이용하여 회전시킬 리스트를 길이 4로하여 생성하고, 각 좌우 정보를 따로 저장해둔다.
5. 동,서 쪽으로 이동할 때 리스트를 좌,우에 저장된 정보를 활용하여 리스트를 갱신함과 동시에 좌,우의 정보도 갱신한다. 
'''

#    동, 서, 북, 남
xi = [1, -1, 0, 0]
yi = [0, 0, -1, 1]

# 현재위치의 지도가 0인지 여부 판별 후, 작업수행
def func(dy, dx):
    global cur_num

    if matrix[dy][dx] == 0:
        matrix[dy][dx] = dice[cur_num]
    else:
        dice[cur_num] = matrix[dy][dx]
        matrix[dy][dx] = 0

    return


N, M, y, x, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 동,서,북,남 => 1,2,3,4
order = list(map(int, input().split()))
# (북,남)으로 회전할 주사위
dice = [0, 0, 0, 0]
# 현재 위치
cur_num = 3
# 오른쪽 면
r = 0
# 왼쪽 면
l = 0

for ord in order:
    dx = x + xi[ord-1]
    dy = y + yi[ord-1]

    if 0 <= dx < M and 0 <= dy < N:
        x = dx
        y = dy
        # print(f'order: {ord}, point: {y,x}')

        if ord == 4:
            cur_num += 3
            cur_num %= 4

            if matrix[dy][dx] == 0:
                matrix[dy][dx] = dice[cur_num]
            else:
                dice[cur_num] = matrix[dy][dx]
                matrix[dy][dx] = 0

        elif ord == 3:
            cur_num += 1
            cur_num %= 4

            if matrix[dy][dx] == 0:
                matrix[dy][dx] = dice[cur_num]
            else:
                dice[cur_num] = matrix[dy][dx]
                matrix[dy][dx] = 0

        elif ord == 1:
            temp_l = dice[cur_num]
            temp_r = dice[(cur_num+2)%4]
            dice[cur_num] = r
            dice[(cur_num+2)%4] = l
            l = temp_l
            r = temp_r

            if matrix[dy][dx] == 0:
                matrix[dy][dx] = dice[cur_num]
            else:
                dice[cur_num] = matrix[dy][dx]
                matrix[dy][dx] = 0

        elif ord == 2:
            temp_r = dice[cur_num]
            temp_l = dice[(cur_num+2)%4]
            dice[cur_num] = l
            dice[(cur_num+2)%4] = r
            r = temp_r
            l = temp_l

            if matrix[dy][dx] == 0:
                matrix[dy][dx] = dice[cur_num]
            else:
                dice[cur_num] = matrix[dy][dx]
                matrix[dy][dx] = 0

        # print(l, dice, r)
        print(dice[(cur_num + 2) % 4])

