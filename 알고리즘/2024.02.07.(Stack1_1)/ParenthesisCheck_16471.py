import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for tc in range(1, T+1):
    str_list = list(input())
    check_list = [0] * len(str_list)
    loc = -1

    check = True
    for s in str_list:
        if s == '(' or s == '{':
            loc += 1
            check_list[loc] = s
        elif s == ')':
            if check_list[loc] == '(':
                check_list.pop(loc)
                loc -= 1
            else:
                check = False
                break
        elif s == '}':
            if check_list[loc] == '{':
                check_list.pop(loc)
                loc -= 1
            else:
                check = False
                break

    if check_list[0] != 0:
        check = False

    if check:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
