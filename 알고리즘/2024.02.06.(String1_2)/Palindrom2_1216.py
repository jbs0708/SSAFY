import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = 10

for tc in range(1, T+1):
    t = int(input())

    list_ = [list(input()) for _ in range(100)]

    max_ = 0
    for i in range(100):
        for j in range(100):
            for k in range(99, -1, -1):
                # 슬라이싱에서 범위를 넘어간다면 그냥 최대 범위까지 나타내고 오류없음
                temp = list_[i][j:j+k]
                if temp == temp[::-1]:
                    max_ = max(max_, len(temp))

    list_90 = list(map(list, zip(*list_)))
    for i in range(100):
        for j in range(100):
            for k in range(99, -1, -1):
                # 슬라이싱에서 범위를 넘어간다면 그냥 최대 범위까지 나타내고 오류없음
                temp = list_90[i][j:j+k]
                if temp == temp[::-1]:
                    max_ = max(max_, len(temp))

    print(f'#{tc} {max_}')