import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T + 1):
    cost = list(map(int, input().split()))
    list_ = list(map(int, input().split()))
    ans = min(sum(list_) * cost[0], cost[3])

    q = deque()
    q.append((0, 0))
    while q:
        curr_cost, curr_month = q.popleft()

        if curr_cost < ans and curr_month < 12:
            # 일간
            q.append((curr_cost + list_[curr_month] * cost[0], curr_month+1))
            # 월간
            q.append((curr_cost + cost[1], curr_month+1))
            # 분기
            q.append((curr_cost + cost[2], curr_month+3))
        elif curr_month >= 12:
            ans = min(curr_cost, ans)

    print(f'#{tc} {ans}')