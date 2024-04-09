import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def count(node):
    global max_
    ans += 1
    if node:
        for n in node:
            count(tree[n])



T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    list_ = list(map(int, input().split()))
    edge = []
    max_ = 0

    tree = [[] for _ in range(E+2)]

    for e in range(0, E*2, 2):
        tree[list_[e]].append(list_[e+1])

    count(tree[N])
    print(f'#{tc} {max_}')