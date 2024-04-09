import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0
    result = {N}
    lim = 1000001
    visited = [False] * lim

    while not M in result:
        ans += 1
        temp = set()
        for i in result:
            if i+1 < lim:
                if not visited[i+1]:
                    visited[i+1] = True
                    temp.add(i + 1)
            if i*2 < lim:
                if not visited[i*2]:
                    visited[i*2] = True
                    temp.add(i*2)
            if not visited[i-1]:
                visited[i-1] = True
                temp.add(i-1)
            if not visited[i-10]:
                visited[i-10] = True
                temp.add(i-10)
        result = temp

    print(f'#{tc} {ans}')
