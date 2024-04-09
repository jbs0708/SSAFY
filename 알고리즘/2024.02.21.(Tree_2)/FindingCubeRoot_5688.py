import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    cube_root = N**(1/3)
    cube_root += 0.000001
    int_value = int(cube_root)
    max_ = int_value ** 3

    if max_ == N:
        print(f'#{tc} {int(cube_root)}')
    else:
        print(f'#{tc} -1')