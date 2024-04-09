import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def operation(node_i):
    if len(list_op[node_i]) == 4:
        a = operation(int(list_op[node_i][2]))
        b = operation(int(list_op[node_i][3]))
        ans = 0
        op = list_op[node_i][1]
        if op == '-':
            ans = a - b
        elif op == '+':
            ans = a + b
        elif op == '/':
            ans = a / b
        elif op == '*':
            ans = a * b
        return ans
    else:
        return int(list_op[node_i][1])


T = 10

for tc in range(1, T + 1):
    N = int(input())
    list_op = []

    for i in range(N):
        temp = list(input().split())
        list_op.append(temp)

    list_op.insert(0, [])
    print(f'#{tc} {int(operation(1))}')