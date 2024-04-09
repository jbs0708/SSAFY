import sys

sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

def binary_search(inputList, N, key):
    global r_cnt
    global l_cnt
    start = 0
    end = N - 1
    while start <= end:
        if l_cnt == 2 or r_cnt == 2:
            return False
        middle = (start+end)//2
        if inputList[middle] == key:
            return True
        elif inputList[middle] > key:
            end = middle - 1
            l_cnt += 1
            r_cnt = 0
        else:
            start = middle + 1
            r_cnt += 1
            l_cnt = 0
    return False


T = int(input())

for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N, M = NM[0], NM[1]

    list_ = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    n_list = []

    for i in range(N):
        n_list.append(min(list_))
        list_.remove(min(list_))

    cnt = 0
    for m in m_list:
        l_cnt = 0
        r_cnt = 0
        if binary_search(n_list, N, m):
            cnt += 1

    print(f'#{tc} {cnt}')