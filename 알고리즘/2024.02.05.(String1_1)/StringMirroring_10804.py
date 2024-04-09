import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T+1):
    str_list = list(input())

    dict = {'p' : 'q', 'b' : 'd', 'd' : 'b', 'q' : 'p'}

    max_ = ''
    for s in str_list:
        max_ += dict[s]

    max_ = max_[::-1]

    print(f'#{tc} {max_}')