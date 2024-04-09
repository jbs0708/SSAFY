import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    temp = list(map(str, input().split()))
    N = int(temp[1])

    list_ = list(map(str, input().split()))
    ans_list = []

    for s in list_:
        if s == 'ZRO':
            ans_list.append(0)
        elif s == 'ONE':
            ans_list.append(1)
        elif s == 'TWO':
            ans_list.append(2)
        elif s == 'THR':
            ans_list.append(3)
        elif s == 'FOR':
            ans_list.append(4)
        elif s == 'FIV':
            ans_list.append(5)
        elif s == 'SIX':
            ans_list.append(6)
        elif s == 'SVN':
            ans_list.append(7)
        elif s == 'EGT':
            ans_list.append(8)
        elif s == 'NIN':
            ans_list.append(9)

    ans_list.sort()

    print(f'#{tc}')
    for i in range(N):
        if ans_list[i] == 0:
            print('ZRO', end=' ')
        elif ans_list[i] == 1:
            print('ONE', end=' ')
        elif ans_list[i] == 2:
            print('TWO', end=' ')
        elif ans_list[i] == 3:
            print('THR', end=' ')
        elif ans_list[i] == 4:
            print('FOR', end=' ')
        elif ans_list[i] == 5:
            print('FIV', end=' ')
        elif ans_list[i] == 6:
            print('SIX', end=' ')
        elif ans_list[i] == 7:
            print('SVN', end=' ')
        elif ans_list[i] == 8:
            print('EGT', end=' ')
        elif ans_list[i] == 9:
            print('NIN', end=' ')
    print()