import sys
from collections import deque

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def make_v2(v1):
    v2 = []
    for i in range(N):
        if not i in v1:
            v2.append(i)

    return v2


def difference(v1, v2):
    global diff

    v1_sum = sum(pi[i] for i in v1)
    diff_temp = abs(pi_sum - v1_sum*2)
    diff = min(diff, diff_temp)
    return


def dfs(loc, visited, v1):
    for i in range(loc, N):
        if not visited[i]:
            visited[i] = 1
            if sum(visited) == N:
                visited[i] = 0
                return
            else:
                v1.append(i)
                if check(v1):
                    v2 = make_v2(v1)
                    if check(v2):
                        difference(v1, v2)
                dfs(i, visited, v1)
                v1.remove(i)
                visited[i] = 0


def check(v1):

    if len(v1) == 1:
        return True
    else:
        visit_v = [0] * N
        q = deque()
        q.append(v1[0])
        visit_v[v1[0]] = 1

        while q:
            line = q.popleft()

            for l in range(N):
                if linked[line][l] == 1 and not visit_v[l] and l in v1:
                    visit_v[l] = 1
                    if sum(visit_v) == len(v1):
                        return True
                    q.append(l)

        if sum(visit_v) == len(v1):
            return True
        else:
            return False


T = int(sys.stdin.readline())

for tc in range(1, T+1):
    N = int(sys.stdin.readline())
    linked = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    pi = list(map(int, sys.stdin.readline().split()))
    pi_sum = 0
    for i in pi:
        pi_sum += i
    v_1 = [0]
    v_2 = [i for i in range(1, N)]
    diff = float('inf')
    if check(v_2):
        difference(v_1, v_2)

    visited = [0] * N
    visited[0] = 1

    dfs(1, visited, v_1)

    print(f'#{tc} {diff}')