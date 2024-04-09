import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    # N: 인원, M: 시간(초), K: 붕어빵 갯수
    N, M, K = map(int, input().split())
    list_ = list(map(int, input().split()))
    # 도착시간 빠른 순으로 정렬
    list_.sort()

    max_ = "Possible"
    # M초 마다 붕어빵이 나옴
    time = M
    for i in range(1, N+1, K):
        # M초가 되기전에 온 사람이거나, 도착한 사람이 커버 가능한 갯수를 넘어간다면
        if list_[i-1] < time:
            # 불가능
            max_ = "Impossible"
            break
        time += M

    print(f'#{tc} {max_}')