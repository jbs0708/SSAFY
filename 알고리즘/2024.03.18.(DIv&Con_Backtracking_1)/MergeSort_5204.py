import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def div_con(list_):
    global cnt

    n = len(list_)

    list_1 = list_[0:n // 2]
    list_2 = list_[n // 2:n]

    if len(list_1) > 1:
        div_con(list_1)
    if len(list_2) > 1:
        div_con(list_2)

    list_1 = sorted(list_1)
    list_2 = sorted(list_2)
    if list_1[len(list_1) - 1] > list_2[len(list_2) - 1]:
        cnt += 1

    return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    list_ = list(map(int, input().split()))
    sorted_list = sorted(list_)
    cnt = 0

    div_con(list_)

    print(f'#{tc} {sorted_list[N//2]} {cnt}')
