import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_ = max(trees)
    growth = [max_ - trees[i] for i in range(N)]
    max_ = 0

    odd_day = 0
    even_day = 0

    for g in growth:
        if g and g % 2 == 1:
            odd_day += 1
            even_day += g//2
        elif g and g % 2 == 0:
            even_day += g//2

    while odd_day < even_day - 1:
        odd_day += 2
        even_day -= 1

    if odd_day > even_day:
        max_ = odd_day * 2 - 1
    elif odd_day == even_day:
        max_ = odd_day * 2
    else:
        max_ = even_day * 2

    print(f'#{tc} {max_}')

