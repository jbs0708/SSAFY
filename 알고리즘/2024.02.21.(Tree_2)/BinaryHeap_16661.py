import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def inserting(n, a):
    # 순차적으로 넣되,
    tree[n] = a
    # 조상의 값과 비교하여
    comp = n // 2
    # 인덱스값이 범위 이내이고 조상보다 값이 작다면
    while comp >= 1 and tree[n] < tree[comp]:
        # 교환
        tree[n], tree[comp] = tree[comp], tree[n]
        # 그 상위값 비교를 위한 인덱스 설정
        n //= 2
        comp //= 2


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = [0 for _ in range(N + 1)]
    list_ = list(map(int, input().split()))

    for i in range(1, N + 1):
        inserting(i, list_[i - 1])

    sum_ = 0
    # 자기자신은 빼고 조상들의 합만구하므로 //2
    n = N // 2
    while n > 0:
        sum_ += tree[n]
        n //= 2

    print(f'#{tc} {sum_}')
