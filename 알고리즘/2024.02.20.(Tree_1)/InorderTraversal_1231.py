import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def inorder(i):
    if not visited[tree[i][0]]:
        if tree[i][2] and not visited[tree[i][0]]:
            inorder(tree[i][2]-1)

        visited[tree[i][0]] = True
        print(tree[i][1], end='')

        if tree[i][3]:
            inorder(tree[i][3]-1)


T = 10

for tc in range(1, T + 1):
    N = int(input())
    visited = [False] * (N+1)

    tree = []
    for i in range(N):
        temp = input().split()
        if len(temp) < 4:
            while len(temp) != 4:
                temp.append(0)

        for n in range(4):
            if type(temp[n]) == str and temp[n].isnumeric():
                temp[n] = int(temp[n])

        tree.append(temp)

    print(f'#{tc} ', end='')
    inorder(0)
    print()