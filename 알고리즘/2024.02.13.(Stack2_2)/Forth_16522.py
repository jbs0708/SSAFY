import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    input_list = input().strip().split()
    max_ = ''
    stack = []

    for c in input_list:
        if c == '.':
            if len(stack) == 1:
                max_ = stack[0]
            else:
                max_ = 'error'
            break

        if c in '+-/*':
            if len(stack) < 2:
                max_ = 'error'
                break
            else:
                b = stack.pop()
                a = stack.pop()

                temp = 0
                if c == '-':
                    temp = a - b
                elif c == '+':
                    temp = a + b
                elif c == '*':
                    temp = a * b
                elif c == '/':
                    temp = a // b  # 항상 나누어 떨어지지만 정수형으로 값을 반환받기 위해 //

                stack.append(temp)
        else:
            stack.append(int(c))

    print(f'#{tc} {max_}')
