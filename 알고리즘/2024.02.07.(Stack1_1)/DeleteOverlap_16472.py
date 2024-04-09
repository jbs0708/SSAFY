import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    str_list = list(input())
    loc = 0

    while loc < len(str_list) - 1:
        if str_list[loc] == str_list[loc+1]:
            str_list.pop(loc)
            str_list.pop(loc)
            if loc >= 1:
                loc -= 1
        else:
            loc += 1

    if len(str_list) == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {len(str_list)}')