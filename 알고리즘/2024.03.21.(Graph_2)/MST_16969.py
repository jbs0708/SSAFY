import sys
import heapq

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 간선 방문 유무 확인
    visited = [0] * (V+1)
    # 간선 목록 리스트
    edge = [[] for _ in range(V+1)]
    ans = 0

    # 간선 정보
    for i in range(E):
        v1, v2, d = map(int, input().split())
        # 양 방향이므로 각 지점을 시작점과 끝점으로 하여 추가
        edge[v1].append([d, v2])
        edge[v2].append([d, v1])

    h = []
    heapq.heappush(h, [0, 0])

    cnt = 0
    while h:
        d, v = heapq.heappop(h)

        if cnt == V+1:
            break

        if visited[v]:
            continue
        else:
            visited[v] = 1
            cnt += 1
            ans += d
            for e in edge[v]:
                nd, nv = e
                if not visited[nv]:
                    heapq.heappush(h, [nd, nv])

    print(f'#{tc} {ans}')
