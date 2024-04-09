import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    string = input()
    s_len = len(string)
    N = 4 + s_len + (s_len-1) * 3

    # 1
    print('..#',end='')
    for i in range(s_len-1):
        print('...#', end='')
    print('..')

    # 2
    for i in range(s_len*2):
        print('.#',end='')
    print('.')

    # 3
    for s in string:
        print(f'#.{s}.',end='')
    print('#')

    # 4
    for i in range(s_len*2):
        print('.#',end='')
    print('.')

    # 5
    print('..#', end='')
    for i in range(s_len - 1):
        print('...#', end='')
    print('..')


