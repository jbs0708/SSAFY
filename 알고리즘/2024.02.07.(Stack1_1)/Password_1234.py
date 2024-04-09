import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = 10

for tc in range(1, T+1):
    N, n_str = input().split()
    str_list = list(n_str)
    loc = 0

    while loc < len(str_list) - 1:
        if str_list[loc] == str_list[loc+1]:
            str_list.pop(loc)
            str_list.pop(loc)
            if loc >= 1:
                loc -= 1
        else:
            loc += 1

    max_ = ''
    for s in str_list:
        max_ += s
    print(f'#{tc} {max_}')