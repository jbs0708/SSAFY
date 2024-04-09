import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

'''
# 특이점
## 빠큐와 나머지 모양을 구분해서 탐색한다.

# 이유
## 빠큐를 제외한 도형은 한붓그리기(선형탐색)로 그리는 것이 가능한데
## 빠큐는 한붓 그리기로 안그려지므로 4방향 빠큐에 대해서 따로 탐색 
'''

# 빠큐를 제외한 모양들을 체크
def checkShapes(y, x, cnt, sum_, exception = -1): # exception: 왔던 방향 제외
    global max_

    cnt += 1

    if cnt > 4:
        max_ = max(max_, sum_)
        return
    sum_ += matrix[y][x]

    for i in range(4):
        if i != exception:
            dx = x + xi[i]
            dy = y + yi[i]
            # 범위체크
            if 0 <= dx < M and 0 <= dy < N:
                checkShapes(dy, dx, cnt, sum_, (i+2)%4) # 왔던 방향을 제외

# 빠큐를 체크
def checkFuck(y, x):
    global max_
    # 각 4방향에 대해서
    for i in range(4):
        # 항상 겹치는 중앙값으로 합계 변수를 초기화
        sum_ = matrix[y][x]
        # 3개의 값을 합산
        for d in range(3):
            dx = x + xi[(i + d) % 4]
            dy = y + yi[(i + d) % 4]
            # 범위체크
            if 0 <= dx < M and 0 <= dy < N:
                sum_ += matrix[dy][dx]

        max_ = max(max_, sum_)


# 행, 열 입력
N, M = map(int, input().split())

# 좌표리스트 입력
matrix = [list(map(int, input().split())) for _ in range(N)]

# 4방향
xi = [1, 0, -1, 0]
yi = [0, 1, 0, -1]

max_ = 0
for y in range(N):
    for x in range(M):
        cnt = 0
        sum_s = 0
        checkShapes(y, x, cnt, sum_s)
        checkFuck(y, x)

print(max_)


