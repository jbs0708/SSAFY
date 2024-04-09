import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = 10

priority = {'*': 2, '+': 1}

for tc in range(1, T + 1):
    N = int(input())
    string = input()

    stack = []
    postfix = ''

    # 후위표기법 변환
    for s in string:
        if s == '+':
            stack.append(s)
        else:
            postfix = postfix + s

    # 후위표기 계산

    print(f'#{tc} {stack.pop()}')
