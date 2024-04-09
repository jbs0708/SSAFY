import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().rstrip().split())
    visited = [False for _ in range(10000)]
    visited[A] = True

    q = deque()
    q.append((A, ''))

    while q:
        a, b = q.popleft()

        if a == B:
            print(b)
            break

        d = (a * 2) % 10000
        if not visited[d]:
            visited[d] = True
            q.append((d, b + 'D'))

        if a == 0:
            s = 9999
        else:
            s = a - 1
        if not visited[s]:
            visited[s] = True
            q.append((s, b + 'S'))

        l = (a // 1000) + (a % 1000) * 10
        if not visited[l]:
            visited[l] = True
            q.append((l, b + 'L'))

        r = (a % 10) * 1000 + (a // 10)
        if not visited[r]:
            visited[r] = True
            q.append((r, b + 'R'))
