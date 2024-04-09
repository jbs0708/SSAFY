from collections import deque
import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    P = input()
    N = int(input())
    inputStr = input()
    inputStr = inputStr[1:len(inputStr)-1]
    q = deque()
    if len(inputStr) > 0:
        str = list(map(int, inputStr.split(',')))
        q = deque(str)

    direction = True
    error = False
    for p in P:
        if p == 'R':
            direction = not direction
        elif p == 'D':
            if q:
                if direction:
                    q.popleft()
                else:
                    q.pop()
            else:
                error = True

    if not error:
        print('[', end='')
        if q:
            if direction:
                print(q.popleft(), end='')
                while q:
                    print(f',{q.popleft()}', end='')
            else:
                print(q.pop(), end='')
                while q:
                    print(f',{q.pop()}', end='')
        print(']')
    else:
        print('error')
