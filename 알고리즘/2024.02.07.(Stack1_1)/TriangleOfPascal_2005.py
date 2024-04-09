import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')

    pri_list = [1] * N
    for row in range(1, N+1):
        temp_list = [1] * N
        for col in range(row):
            if col == 0 or col == row-1:
                print(1, end=' ')
            else:
                temp = pri_list[col-1] + pri_list[col]
                print(temp, end=' ')
                temp_list[col] = temp
        pri_list = temp_list
        print()