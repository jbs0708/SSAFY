import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = [list(map(str, input().split())) for _ in range(N)]
    deg_90 = [list(reversed(list_)) for list_ in list(zip(*num_list))]
    deg_180 = [list(reversed(list_)) for list_ in list(zip(*deg_90))]
    deg_270 = [list(reversed(list_)) for list_ in list(zip(*deg_180))]
    max_ = deg_90 + deg_180 + deg_270
    # print(ans)

    print(f'#{tc}')
    for i in range(N):
        for j in range(3):
            print(''.join(max_[i + j * N]), end=' ')
        print()


