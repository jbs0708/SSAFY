import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 밖에서의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 안에서의 우선순위

T = 10

for tc in range(1, T+1):
    N = int(input())
    top = -1
    stack = [0] * N

    fx = input()
    postfix = ''

    for tk in fx:
        # 여는 괄호 push, top원소보다 우선순위가 높으면 push
        if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
            top += 1
            stack[top] = tk
        elif tk in '*/+-' and isp[stack[top]] >= icp[tk]:  # 연산자이고 top원소보다 우선순위가 높지않으면
            while isp[stack[top]] >= icp[tk]:  # top원소의 우선순위가 낮을 때까지 pop
                top -= 1
                postfix += stack[top + 1]
            top += 1
            stack[top] = tk
        elif tk == ')':  # 닫는 괄호면, 여는 괄호를 만날때까지 pop
            while stack[top] != '(':
                top -= 1
                postfix += stack[top + 1]
            top -= 1  # 여는 괄호 pop해서 버림
            stack[top+1]
        else:
            postfix += tk

    stack_ = []
    for i in postfix:
        if i in '+*':
            b = stack_.pop()
            a = stack_.pop()
            if i == '+':
                stack_.append(a + b)
            else:
                stack_.append(a * b)
        else:
            stack_.append(int(i))

    print(f'#{tc} {stack_.pop()}')