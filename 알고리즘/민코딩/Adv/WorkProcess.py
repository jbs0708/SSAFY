import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tasks = []
    pre = [[0]]
    for i in range(N):
        list_ = list(map(int, input().split()))
        tasks.append(list_[0])
        if list_[1] != 0:
            pre.append(list_[2:])


    ans = 0


    print(f'#{tc} {ans}')
