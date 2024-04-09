T = int(input())

for tc in range(T):
    temp = input()
    dict_1 = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
              'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

    dict_2 = {value: key for key, value in dict_1.items()}

    list_ = sorted(dict_1[num] for num in list(input().split()))

    print(f'#{tc + 1}')
    print(*(dict_2[num] for num in list_), end=' ')
    print()