import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = 10

for tc in range(1, T + 1):
    t = input()
    q = deque(map(int, input().split()))

    i = 1
    while True:
        temp = q.popleft()
        temp -= i
        if temp <= 0:
            temp = 0
            q.append(temp)
            break
        else:
            q.append(temp)
            i += 1
            if i > 5:
                i -= 5

    print(f'#{tc} ', *q)



