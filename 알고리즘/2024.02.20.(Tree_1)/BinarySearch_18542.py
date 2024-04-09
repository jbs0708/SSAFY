import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def inorder(v):
    global num
    if v < max_:
        # (가장 좌측 가장 밑단이 1부터 시작 , 각 레벨의 좌측은 1부터 2**n)
        # (1, 2 ** n)
        inorder(v * 2)

        # 해당노드(위아래의 부모노드)에 [왼쪽 자식 +1]을 채움
        tree[v] = num
        num += 1

        # 우측 자식 노드로 분기
        inorder(v * 2 + 1)
    else:
        return


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    max_ = N+1
    num = 1
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')
