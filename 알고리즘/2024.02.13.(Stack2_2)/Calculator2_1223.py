import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = 10

priority = {'*': 2, '+': 1}

for tc in range(1, T + 1):
    N = int(input())
    input_str = input()
    top = -1
    stack = []
    postfix = ''

    top = -1
    for tk in input_str:
        if tk.isnumeric():
            postfix += tk
        elif tk == '*':
            while stack and stack[-1] == '*':
                postfix += stack.pop()
            stack.append(tk)
        elif tk == '+':
            while stack:
                postfix += stack.pop()
            stack.append(tk)
    while stack:
        postfix += stack.pop()

    for i in postfix:
        if i in '+*':
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a+b)
            else:
                stack.append(a*b)
        else:
            stack.append(int(i))

    print(f'#{tc} {stack.pop()}')
