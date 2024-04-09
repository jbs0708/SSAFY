import sys

sys.stdin = open("input.txt")
sys.stdout = open("output.txt", 'w')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    str_ = input()
    list_ = []
    for s in str_:
        list_.append(int(s))

    cnt = 0
    max_ = 0
    if list_[0] == 1:
        cnt += 1
    for n in range(1, N):
        if list_[n] == 1:
            cnt += 1
            if max_ < cnt:
                max_ = cnt
        else:
            cnt = 0

    print(f'#{tc} {max_}')