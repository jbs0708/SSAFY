for T in range(int(input())):
    a = input()
    str_list = input().split()
    str_num = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    str_list.sort(key=lambda x: str_num[x])

    print(f'#{T + 1} {" ".join(str_list)}')