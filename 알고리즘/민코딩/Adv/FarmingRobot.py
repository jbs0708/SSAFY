import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def dfs(y, x, d, temp, day, seed):
    if martix[y][x] == 0:



di = [0, 1, 2, 3]
xi = [1, 0, -1, 0]
yi = [0, -1, 0, 1]


T = int(input())

for tc in range(1, T+1):
    N, M = int(input())
    martix = [list(map(int, input().split())) for _ in range(N)]
    max_d = [0] * M
    ans = 0

    for i in range(N):
        for j in range(N):
            if not martix[i][j]:
                for d in range(4):
                    dfs(i, j, di[d], 0, 0)



    ans = 0


    print(f'#{tc} {ans}')
