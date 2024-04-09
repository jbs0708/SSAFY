import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cnt = M % N
    list_ = list(map(int, input().split()))

    print(f'#{tc} {list_[cnt]}')
