import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def operation(node_i):
    if node_i * 2 < N:
        a = operation(node_i*2)
        b = operation(node_i*2 + 1)
        tree[node_i] = a + b
    elif node_i * 2 == N:
        a = operation(node_i*2)
        tree[node_i] = a

    if node_i == L:
        print(f'#{tc} {tree[node_i]}')
        return tree[node_i]
    else:
        return tree[node_i]


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]

    for m in range(M):
        temp = list(map(int, input().split()))
        tree[temp[0]] = temp[1]

    operation(1)



