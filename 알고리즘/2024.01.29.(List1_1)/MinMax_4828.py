import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    list_ = list(map(int, input().split()))
    max_ = max(list_)
    min_ = min(list_)

    print(f'#{tc} {max_-min_}')