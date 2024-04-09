import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


T = int(input())

for _ in range(T):
    t, l = map(str,input().split())
    lst = list(map(str, input().split()))

    str_dict = {"ZRO" : 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR":4, "FIV":5,
                "SIX":6, "SVN":7, "EGT": 8, "NIN": 9}

    # 정렬 기준을 딕셔너리의 value 값으로
    lst.sort(key = str_dict.get)
    print(t)
    print(*lst)