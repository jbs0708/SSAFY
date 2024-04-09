seq_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for tc in range(1, T + 1):
    t, N = map(str, input().split())
    list_ = list(map(str, input().split()))
    num_list = [0] * 10

    for i in list_:
        num_list[seq_list.index(i)] += 1

    print(f'#{tc}')
    for i in range(len(num_list)):
        print((seq_list[i] + ' ') * num_list[i], end='')
    print()