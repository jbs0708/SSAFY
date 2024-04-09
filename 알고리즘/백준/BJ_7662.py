import sys
import heapq

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    visited = [False] * N
    min_h, max_h = [], []

    for i in range(N):
        o, n = input().split()
        num = int(n)
        if o == 'I':
            heapq.heappush(min_h, (num, i))
            heapq.heappush(max_h, (-num, i))
            visited[i] = True
        elif o == 'D':
            if num == 1:
                while max_h and not visited[max_h[0][1]]:
                    heapq.heappop(max_h)
                if max_h:
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)
            elif num == -1:
                while min_h and not visited[min_h[0][1]]:
                    heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)

    while min_h and not visited[min_h[0][1]]:
        heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]:
        heapq.heappop(max_h)

    if min_h and max_h:
        print(f'{-1 * max_h[0][0]} {min_h[0][0]}')
    else:
        print('EMPTY')


